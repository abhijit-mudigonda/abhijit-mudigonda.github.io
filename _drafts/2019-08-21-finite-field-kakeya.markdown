## The Kakeya Set Conjecture
This is based on a [blog post][https://terrytao.wordpress.com/2008/11/27/the-kakeya-conjecture-and-the-ham-sandwich-theorem/] by Terence Tao. 

### Hausdorff and Minkowski-Bouligand Dimension
{% include defbox.html thmname="Definition" thmnum=1 thmtxt="Let $X$ be a set in a Euclidean (metric) space. Let $N(\epsilon)$ be the number of boxes of side length $\epsilon$ (balls of radius $\epsilon$) needed to cover $X$. Then, the **Minkowski-Bouligand dimension** of a set $X$ is defined as
    \begin{equation}
        \lim_{\epsilon \rightarrow 0} \log_{\frac{1}{\epsilon}} N(\epsilon).
    \end{equation}

    If the limit doesn't exist, we can consider the upper and lower box (ball) covering dimensions to be the limit superior and limit inferior of this sequence, respectively." %} <br />

Intuitively, if our boxes have side length $\frac{1}{n}$ then we need $Cn^d$ boxes to cover $X$, where $d$ is the normal notion of dimension. This definition more or less captures $d$. 

{% include exbox.html thmname="Example" thmnum=1 thmtxt="
- Euclidean space has Minkowski dimension $n$.
- $\Q$ has dimension $1$ because its closure is $\R$
- The Cantor set has dimension $\log_2 3$. To (nonrigorously) see this, note that the subsequence of $\epsilon = \frac{1}{3^n}$ always satisfies $\log_{\frac{1}{\epsilon}} N(\epsilon)$ and the overall function is monotonic in $\epsilon$.

" %} <br />

{% include defbox.html thmname="Definition" thmnum=1 thmtxt="Let $X$ be a set in a metric space. Let $\cB$ be the set of collections of balls $B_i$ of radius $r_i$ that cover $X$. Then, the $d$-dimensional **Hausdorff content** of $X$ is defined as
    $$
        \cC_H^d(X) = \inf_{\cB} \{\sum_i r_i^d\}.
    $$

    The **Hausdorff measure** of $X$ is defined as
    $$
        \inf_d \{d \mid \cC_H^d = 0\}.
    $$" %} <br />

I'm not sure what the intuition is here but it feels to me like the idea that the sum of a function's values at lattice points of $\R^n$ converges when the function falls off slower than $\frac{1}{r^n}$ (so for $\R$ we need it to be slower than $\frac{1}{x}$). 

### Motivation

The conjecture was motivated by the following problem.

{% include exbox.html thmname="Problem" thmnum=1 thmtxt="Suppose we wish to rotate a unit-length needle in $\R^2$. What is the minimum measure of the area that it sweeps out?" %} <br />

As it turns out, the minimum measure is $0$ but the dimension is necessarily $2$! However, this question becomes significantly harder in higher dimension. 

{% include thmbox.html thmname="Conjecture" thmnum=1 thmtxt="[Kakeya set conjecture]
    Let $n \geq 1$ and $X \subseteq \R^n$ contain a unit line segment in every direction - such sets are known as **Kakeya sets** or **Besikovitch sets**. Then, $X$ has Hausdorff and Minkowski dimension equal to $n$." %} <br />

## Proof of the Finite Field Kakeya Conjecture

This is based on  Terence Tao's \href{https://terrytao.wordpress.com/2008/03/24/dvirs-proof-of-the-finite-field-kakeya-conjecture/}{blog post}. 
{% include thmbox.html thmname="Theorem" thmnum=1 thmtxt="[Finite field Kakeya conjecture]
    Let $X \subset \F_q^n$. Then, $X$ has cardinality at least $c_nq^n$ where $c_n$ depends only on $n$." %} <br />

This corresponds loosely to the earlier notion of Minkowski dimension. 

*Proof*: [Zeev Dvir]
    The proof follows from two pretty simple lemmas. 
    {% include thmbox.html thmname="Lemma" thmnum=1 thmtxt="Let $F$ be a field. Take $X \subset F^n$ such that $|X| < \binom{n+d}{d}$. Then, there exists a degree $d$ polynomial over $F^n$ vanishing on $X$." %} <br />
    *Proof*: 
        Consider the map from the space of degree $d$ polynomials to the space of functions on $X$ that sends a polynomial $f$ to $f|_X$. This is a linear map of vector spaces. The space of degree $d$ $n$-variate polynomials has dimension $\binom{n+d}{d}$ by stars-and-bars, and the space of functions on $X$ has dimension $|X| < \binom{n+d}{d}$. Thus, the map is not injective and some polynomial is $0$ everywhere. 
        
    

    {% include thmbox.html thmname="Lemma" thmnum=1 thmtxt="No nonzero polynomial of degree less than $q$ vanishes on a Kakeya set." %} <br />

    *Proof*: 
        Suppose for contradiction there's a degree $d \leq q-1$ polynomial that vanishes on the entire set. Then, for any $v \in \Fqn$, there's a $y$ such that $P(y+tv) = 0$ for all $t \in \Fq$. If we treat $P(y+tv)$ as a univariate polynomial in $t$, we see that it's of degree less than $q$ but vanishes at $q$ points and thus must be identically zero. Let's write $P = \sum_i P_i$ where $P_i$ is the $i^{\t{th}}$ homogeneous part. The coefficient of $t^d$ is $P_d(v)$, and thus $P_d(v) = 0$ for all $v \in \Fqn$. However, $P_d$ is degree $d \leq q-1$ and by the Schwarz-Zippel lemma it cannot be zero at more than a $\frac{q-1}{q}$ fraction of points, a contradiction. 
    

    Putting these both together, we see that if $X$ is a Kakeya set, 
    $$
        |X| > \binom{n+q-1}{n}
    $$

    because otherwise there would be a polynomial of degree $q-1$ or less that vanished on it. 
    




