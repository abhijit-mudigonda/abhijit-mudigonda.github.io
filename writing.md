---
layout: page
title: Mathematics
permalink: /math/
---

I am interested in computational complexity, combinatorics, and number theory. 

##Expository Writing

Here are some things I wrote as an undergraduate student. 

- Profinite Groups, Infinite Galois Theory, and an application to Kummer Theory, written for 18.704 (Seminar in Algebra), taught by Prof. Bjorn Poonen. 
- An overview of the proofs of sphere packing in dimensions 8 and 24. Written for 18.786 (Number Theory II), taught by Prof. Wei Zhang, and loosely following [this][cohn-spheres] survey by Henry Cohn
- The official [course notes][18218-notes] to 18.218 (Combinatorics of the Grassmannian) taught by Prof. Alex Postnikov.
##Current Research

My current work, with Professor [Ryan Williams][ryan-williams] is in computational complexity. Specifically, I'm thinking about the following problems:

- \textbf{Quantum Complexity Theory:} 
    - Can we show that there are problems computable by linear time \\(\mathsf{QMA}\\) machines that are not computable by logspace machines using \\(n^c)\\ time for \\(c > 2)\\, akin to weaker results for nondeterministic linear time in the classical setting? *(yes! We can use Grover search to efficiently remove small quantifiers to get \\(c \approx 2.36\\), experimentally verified with Python code [here][automated-lbs])*
    - Can we "speed up" \\(\mathsf{BQP}\\) computations by passing to higher levels in the quantum polynomial hierarchy, akin to speedup results used for time-space lower bounds against nondeterministic linear time in the classical setting? 
    - Is there a way to perform amplification of \\(\mathsf{QMA}\\) machines without increasing the length of Merlin's witness and while also guaranteeing that all initially valid witnesses for a given input stay valid witnesses for this input? See [this][better-qma-amp] StackExchange question for more details.
- \textbf{Counting and Randomized Complexity}
    - What is the best degree for a polynomial threshold function of \\(\mathsf{AND}_s \mathsf{MAJ}_t\\), the conjunction of \\(s\\) majorities each of fan-in \\(t\\)? Can we use this to say things about \\(\mathsf{PP}\\)?[O'Donnell and Servedio][ptf-lb] have a lower bound for the \\(s=2)\\ case, while [Beigel et al.][BRS] and [Alman et al. ][acw-ptfs] give upper bounds using rational approximators and Chebyshev polynomials respectively. 
    - Can we represent a conjunction of \\(b\\) bounded-error randomized machines each with runtime \\(t\\) using unbounded-error randomized machines taking runtime \\(2^{\frac{b}{2}}(b+t)\\)? Note that this is a quadratic speedup for quantifier removal over brute force, akin to the speedup of Grover's algorithm for quantum search. *(yes! we can use [robust][robust] [approximating polynomials][algpoly] for \\(\mathsf{AND}\\))*
- \textbf{Circuit Complexity}
    - What are ways to turn arithmetic circuits into Boolean circuits? Assuming the Generalized Riemann Hypothesis, a lemma of [Koiran][koiran-lem] can be used to, given an arithmetic circuit with complex weights, obtain a Boolean circuit on the same inputs that agrees with the arithmetic circuit \\(\mod p\\) for some "not-too-large" \\(p\\). [Fournier et al.][fournier] obtain arithmetic circuit lower bounds by using this lemma to convert the arithmetic circuits in question to Boolean circuits and applying Boolean circuit lower bounds. Can we improve this procedure further, either by improving Koiran's result or by coming up with new ways to do this conversion? 

[18218-notes]: https://www.overleaf.com/read/zbrxffmrqbvm
[postnikov-site]: https://math.mit.edu/~apost/
[ryan-williiams]: https://people.csail.mit.edu/rrw/
[robust]: http://web.cs.ucla.edu/~sherstov/pdf/robust.pdf
[algpoly]: https://arxiv.org/abs/1801.04607]
[better-qma-amp]: https://quantumcomputing.stackexchange.com/questions/8586/better-in-place-amplification-of-qma
[BRS]: http://www.cs.columbia.edu/~rocco/Teaching/S12/Readings/BRS.pdf
[acw-ptfs]: https://arxiv.org/abs/1608.04355
[koiran-lem]: https://pdfs.semanticscholar.org/d4e6/87c5dc96a0e4fd47465792f7b6f694a85e7a.pdf
[fournier]: https://arxiv.org/pdf/1304.5910.pdf
[ptf-lb]: https://www.cs.cmu.edu/~odonnell/papers/ptf-degree.pdf
[automated-lbs]: https://github.com/abhijit-mudigonda/automated-alternating-lbs

##Past Research



