---
layout: page
mathjax: true
title: Mathematics
permalink: /math/
---


I am interested in computational complexity, combinatorics, and number theory. 

### Expository Writing

Here are some things I wrote as an undergraduate student.  

- [Profinite Groups, Infinite Galois Theory, and an application to Kummer Theory]({{ site.url }}/pdfs/infgalois.pdf): Term paper for 18.704 (Seminar in Algebra), taught by Prof. Bjorn Poonen. 
- [Sphere Packing in 8 Dimensions]({{ site.url }}/pdfs/sphere-packing.pdf): Written for 18.786 (Number Theory II), taught by Prof. Wei Zhang, and loosely following [this][cohn-spheres] survey by Henry Cohn
- The official [course notes][18218-notes] to 18.218 (Combinatorics of the Grassmannian), taught by Prof. Alex Postnikov.


### Current Research

My current work, with Professor [Ryan Williams][ryan-williams], is in computational complexity. Specifically, I'm thinking about the following problems:

- **Quantum Complexity Theory**
    - Can we show that there are problems computable by linear time $$ \mathsf{QMA} $$ machines that are not computable by logspace machines using \\(n^c\\) time for \\(c > 2\\), improving upon weaker results for nondeterministic linear time in the classical setting? **(Yes! We can efficiently remove small quantifiers using Grover search, yielding \\(c \approx 2.36\\). This was experimentally verified with [Python code][automated-lbs])**
    - Is there a generalization of Grover's algorithm to inversion of quantum functions? Normally, Grover search will, given oracle access to a function $f: \\{0,1\\}^n \rightarrow \\{0,1\\}$, find an $x$ such that $f(x) = 1$ with high probability if such an $x$ exists. **(Yes! We can Grover search even when we replace the oracle with a quantum function that may output a superposition of $\|0\rangle$ and $\|1\rangle$, and our goal is to (with high probability) find $$x \in \{0,1\}^n$$ such that $\Pr[f(x) = 1] \geq \frac{2}{3}$. [Here]({{ site.url }}/pdfs/quantum-grover.pdf) is unedited writeup of a more general result, allowing $f$ to have an auxiliary quantum input. I'm not sure if this is useful outside my application, but if it is you should let me know!)**
    - Can we "speed up" \\(\mathsf{BQP}\\) computations by passing to higher levels in the quantum polynomial hierarchy, akin to speedup results used for time-space lower bounds against nondeterministic linear time in the classical setting? 
    - Is there a way to perform amplification of \\(\mathsf{QMA}\\) machines without increasing the length of Merlin's witness and while also guaranteeing that all initially valid witnesses for a given input stay valid witnesses for this input? See [this][better-qma-amp] StackExchange question for more details.
- **Counting and Randomized Complexity**
    - Can we represent a conjunction of \\(b\\) bounded-error randomized machines each with runtime \\(t\\) using unbounded-error randomized machines taking runtime \\(2^{\frac{b}{2}}(b+t)\\)? Note that this is a quadratic speedup for quantifier removal over brute force, akin to the speedup of Grover's algorithm for quantum search. **(Yes! we can use [robust][robust] [approximating polynomials][algpoly] for \\(\mathsf{AND}\\))**
    - What is the best degree for a polynomial threshold function of \\(\mathsf{AND}_s \mathsf{MAJ}_t\\), the conjunction of \\(s\\) majorities each of fan-in \\(t\\)? Can we use this to say things about \\(\mathsf{PP}\\)? [O'Donnell and Servedio][ptf-lb] have a lower bound for the \\(s=2\\) case, while [Beigel et al.][BRS] and [Alman et al. ][acw-ptfs] give upper bounds using rational approximators and Chebyshev polynomials respectively. 
- **Circuit Complexity**
    - 
    - What are ways to turn arithmetic circuits into Boolean circuits? Assuming the Generalized Riemann Hypothesis, a result of Koiran lets us turn an arithmetic circuit with complex weights into a Boolean circuit on the same inputs that agrees with the arithmetic circuit modulo $p$ for some “not-too-large” prime $p$. The proof (eventually) uses the Dedekind-Kummer theorem and the prime number theorem for number fields to upper bound $a$ such that a certain univariate polynomial has a root modulo some prime $p$ less than $a$. Loosely, Dedekind-Kummer is used to  Can we improve this procedure further, either by improving Koiran's result or by coming up with new ways to do this conversion? I've tried to use ideas from Gr\"obner basis theory to improve the reduction to this polynomial. I've also tried analyzing the failure mode of Dedekind-Kummer when studying extensions of primes $p$ that are not prime to the conductor, 
- **Graph Algorithms**
    - Can we asymptotically improve the runtime of algorithms for detecting Hamiltonian cycles in directed graphs using polynomial identity tests? Dynamic programming yields $$ O(n^22^n) $$, so we wish to reduce the base of the exponent below $$2$$. I contributed to the analysis of the multilinear Schwartz-Zippel lemma and its applications to the Hamiltonian cycle polynomial. I've also written [code][ham-code] to study Hamiltonian cycles in dense graphs. 

### Past Research

- (with Professor Ryan Williams) Building on [B&uuml;rgisser and Cooks][burgisser-cooks], I showed containments of the Boolean parts of uniform versions of $$\mathsf{VP}$$ and $$\mathsf{VNP}$$ within well-studied Boolean complexity classes. [Here]({{ site.url }}/pdfs/uniformvnp.pdf) is an unedited writeup. 
- (with Professor Dhruv Ranganathan) Consider a linear space $$ L \subset \mathbb{A}^n $$. Because $$\mathbb{A}^n$$ embeds naturally in the product of projective lines $(\mathbb{P}^1)^n$, we can consider the closure $\tilde{L}$ of $L$ in $(\mathbb{P}^1)^n$. [Ardila and Boocher][ardila-boocher] showed that much of the algebraic structure of $$\tilde{L}$$, including the $$\mathbb{Z}^n$$-multidegree, can be expressed in terms of the properties of the matroid associated with $$L$$. I studied and proved the generalization of this to the case of arbitrary projective compactifications (i.e. any $$\prod \mathbb{P}^{a_i}$$ where the $$a_i$$ sum to $$n$$), but it had by then just been proven as a corollary of [Scholten et al.][scholten]. 

[18218-notes]: https://www.overleaf.com/read/zbrxffmrqbvm
[postnikov-site]: https://math.mit.edu/~apost/
[ryan-williams]: https://people.csail.mit.edu/rrw/
[robust]: http://web.cs.ucla.edu/~sherstov/pdf/robust.pdf
[algpoly]: https://arxiv.org/abs/1801.04607]
[better-qma-amp]: https://quantumcomputing.stackexchange.com/questions/8586/better-in-place-amplification-of-qma
[BRS]: http://www.cs.columbia.edu/~rocco/Teaching/S12/Readings/BRS.pdf
[acw-ptfs]: https://arxiv.org/abs/1608.04355
[koiran-lem]: https://pdfs.semanticscholar.org/d4e6/87c5dc96a0e4fd47465792f7b6f694a85e7a.pdf
[fournier]: https://arxiv.org/pdf/1304.5910.pdf
[ptf-lb]: https://www.cs.cmu.edu/~odonnell/papers/ptf-degree.pdf
[automated-lbs]: https://github.com/abhijit-mudigonda/automated-alternating-lbs
[cohn-spheres]: https://arxiv.org/abs/1611.01685
[burgisser-cooks]: https://link.springer.com/chapter/10.1007/978-3-662-04179-6_4
[ardila-boocher]: https://arxiv.org/abs/1312.6874
[scholten]: https://arxiv.org/abs/1804.02029
[ham-code]: https://github.com/abhijit-mudigonda/directed-ham-cycles

