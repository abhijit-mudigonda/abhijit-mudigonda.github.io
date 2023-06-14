#!/usr/bin/env python

import re
from typing import Any, Dict, List, Tuple
import argh

@argh.arg("tex_filename", help="name of .tex file to convert", type=str)
def tex2markdown(tex_filename: str):
    # one pass, line by line
    # - if the line is \begin{env} for one of a specific set of envs,
    #    - grab env and whatever's in the [] if there is one. 
    #    - increment the counter
    #    - store them in "current env" variables and raise a flag
    #    - clear the string variable
    # - if the line is \end{env} then 
    #    - make a boxstring with the current values of env, content, and counter
    #    - add the boxstring to the file
    #    - lower the flag
    # - if the env flag is up, write the line to the string. otherwise, write to file

    filename, ext = tex_filename.split(".")
    assert ext == "tex"
    tex_file = open(tex_filename, 'r')
    md_file = open(f"{filename}.md", 'w')

    envs = {
            "theorem": ("Theorem", "blue"),
            "proposition": ("Proposition", "blue"),
            "conjecture": ("Conjecture", "blue"),
            "claim": ("Claim", "blue"),
            "fact": ("Fact", "blue"),
            "lemma": ("Lemma", "blue"),
            "corollary": ("Corollary", "blue"),
            "definition": ("Definition", "green"),
            "example": ("Example", "purp")
            }

    env_flag = False
    align_star_flag = False

    env_counter = 0
    env_contents = ""
    env_name = ""
    env_desc = ""
    env_color = ""


    doc_flag = False

    md_file.write("---\n")
    md_file.write(f"title: {filename}\n")
    md_file.write(f"draft: true\n")
    md_file.write("---\n")
    for line in tex_file:
        # throw out all lines before \begin{document}
        if not doc_flag:
            doc_match = re.search(r'\\begin{document}', line)
            if doc_match:
                doc_flag = True

        if not doc_flag:
            continue

        # the line break character \\ must always be replaced by
        # \\\\ for escaping reasons in KaTeX.
        # if we are in an align* environment, we want to precede
        # each new line with the \nonumber tag

        # this should be early because otherwise it will trigger
        # on escaped backslashes introduced later

        if align_star_flag:
            line = re.sub(r'\\\\', r'\\nonumber \\\\\\\\', line)
        else:
            line = re.sub(r'\\\\', r'\\\\\\\\', line)

        #remove \begin{document}
        line = re.sub(r'\\begin\{document\}', '', line)

        #remove \end{document}
        line = re.sub(r'\\end\{document\}', '', line)


        #remove \maketitle
        line = re.sub(r'\\maketitle', '', line)

        # turn \item into - 
        line = re.sub(r'\\item', r'-', line)

        # turn \# into \\##
        line = re.sub(r'\\#', r'\\\#', line)

        # turn \[ or \] into $$
        line = re.sub(r'\\\[', r'$$', line)
        line = re.sub(r'\\\]', r'$$', line)

        # turn \{ into \lbrace and \} into \rbrace
        line = re.sub(r'\\\{', r'\\lbrace', line)
        line = re.sub(r'\\\}', r'\\rbrace', line)

        # turn \section{.*}, \subsection, or \subsubsection into the
        # appropriate markdown headers. 
        # the choices of ###, ####, and ##### are based on the way
        # the different headers are processed in static/css/typography.css
        line = re.sub(r'\\section{(.+?)}', r'#### \1', line)
        line = re.sub(r'\\subsection{(.+?)}', r'##### \1', line)
        line = re.sub(r'\\subsubsection{(.+?)}', r'###### \1', line)

        # turn \textbf{} into ** **
        line = re.sub(r'\\textbf{(.+?)}', r'**\1**', line)
        
        # turn \textbf{} into * *
        line = re.sub(r'\\textit{(.+?)}', r'*\1*', line)

        # remove \label{.*}
        line = re.sub(r'\\label{(.+?)}', '', line)

        # replace \cref{.*} or ~\cref{.*} with TODO
        line = re.sub(r'.\\cref{(.+?)}', r' TODO REF \1', line)

        # remove begin{itemize} or end{itemize}
        line = re.sub(r'\\begin{itemize}', '', line)
        line = re.sub(r'\\end{itemize}', '', line)

        
        # replace \begin{proof} with ***Proof***:
        line = re.sub(r'\\begin{proof}', '***Proof***:', line)

        #replace \begin{remark} with ***Remark***:
        line = re.sub(r'\\begin{remark}', '***Remark***', line)

        #replace \end{proof} with $\Box$
        line = re.sub(r'\\end{proof}', r'$\\Box$', line)
        
        #remove \end{remark}
        line = re.sub(r'\\end{remark}', '', line)

        #replace \href{a}{b} with [b](a)
        line = re.sub(r'\\href{(.+?)}{(.+?)}', r"\[\2\](\1)", line)

        begin_match = re.search(r'\\begin{(.+?)}', line)
        if begin_match:
            env = begin_match.group(1)
            if env in envs.keys():
                assert not env_flag
                tag = env
                env_flag = True
                env_counter += 1
                env_name = envs[env][0]
                env_color = envs[env][1]
                env_contents = ""
                desc_match = re.search('\[(.+?)\]', line)
                if desc_match:
                    desc = desc_match.group(1)
                else:
                    desc = None
                line = ""
            if env == "align*":
                assert not align_star_flag
                align_star_flag = True
                line = re.sub(r'\\begin{align\*}', r'\\begin{align}', line)


        end_match = re.search(r'\\end{(.+?)}', line)
        if end_match:
            env = end_match.group(1)
            if env in envs.keys():
                assert env_flag 
                assert env == tag
                bs = boxString(
                        env_color, 
                        env_name,
                        env_counter,
                        env_desc,
                        env_contents
                )
                md_file.write(bs)
                env_flag = False
                line = ""

            if env == "align*":
                assert align_star_flag
                align_star_flag = False
                line = re.sub(r'\\end{align\*}', r'\\end{align}', line)



        if env_flag:
            env_contents += line
        else:
            md_file.write(line)

def boxString(color: str, name: str, counter: int, desc: str, contents: str) -> str:
    contents = re.sub(r'\n', "", contents)
    if desc == "":
        return f"""{{{{< 
                    {color}box  
                    envname="{name}"  
                    envnum="{counter}"   
                    envdesc=""  
                    envtxt="{contents}" 
                >}}}}"""
    else:
        return f"""{{{{< 
                    envbox  
                    envname="{name}"  
                    envnum="{counter}"  
                    envdesc=" ({desc})"  
                    envtxt="{contents}" 
                }}}}"""

argh.dispatch_command(tex2markdown) 
