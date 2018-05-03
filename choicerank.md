---
layout: default
linkhome: yes
lastedit: 2018-05-02
title: ChoiceRank
---

**ChoiceRank** is an algorithm that estimates the *transition probabilities*
along the edges of a network based on the networks's *structure* and on the
*traffic* at each node of the network. For example, it can be used to estimate
the probability of users clicking on any link of a [Wikipedia page][1], given a
hyperlink graph (such as [this one][2]) and the [number of views][3] each page
got.

<p>
<img src="/img/choicerank/problem.png" class="img-fluid mx-auto d-block" alt="The ChoiceRank problem." />
</p>

The algorithm and the underlying model are described in the following paper:

{% include paper.html key="maystre2017choicerank" %}

There are two implementations of ChoiceRank available at the moment.

- **Python**: the [choix][4] library provides an implementation that is
  well-tested an easy to use, and that scales seamlessly to graphs containing
  up to a few million nodes. Check out [this Jupyter notebook][5] to get
  started.
- **Rust**: for very large graphs, there is an [experimental implementation][6]
  of ChoiceRank written in Rust that is computationally very efficient (it is
  based on Frank McSherry's code for [COST][7]). Documentation is a bit lacking
  at the moment, drop me a line if you need help!

[1]: https://en.wikipedia.org/wiki/Page_(paper)
[2]: https://snap.stanford.edu/data/enwiki-2013.html
[3]: https://tools.wmflabs.org/pageviews/?project=en.wikipedia.org&platform=all-access&agent=user&range=latest-20&pages=Page_(paper)
[4]: https://github.com/lucasmaystre/choix
[5]: https://github.com/lucasmaystre/choix/blob/master/notebooks/choicerank-tutorial.ipynb
[6]: https://github.com/lucasmaystre/COST/tree/choicerank
[7]: http://www.frankmcsherry.org/graph/scalability/cost/2015/01/15/COST.html
