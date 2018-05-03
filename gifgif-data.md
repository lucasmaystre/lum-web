---
layout: default
linkhome: yes
lastedit: 2017-07-07
title: GIFGIF Data
---

[GIFGIF][1] is a project from the MIT Media Lab which aims at understanding the
emotional content of animated GIF images. Visitors on the web site are faced
with two images and a question of the form: *Which image better expresses
happiness (pride / fear / ...)?* In total, 17 different emotions are covered.

<p>
<img src="/img/gifgif-data/hXVmUL3DV3gZy.gif" class="img-fluid" alt="Example image from the dataset." />
</p>

A dataset of pairwise comparison outcomes was graciously provided by the
[GIFGIF team][2]. It consists of **2.7+ million** pairwise comparisons over
**6170** animated GIFS, and consists of all the data until January
21<sup>st</sup>, 2015.

- [Dataset, version 1][3] (CSV compressed with <code>gzip</code>, 52.2 MiB)
- [GIF images, version 1][4] (TAR archive, 5.3 GiB)

You might also be interested in [this Jupyter notebook][5] which illustrates
how to read and process the CSV file. Finally, note that this dataset was used
in the following paper:

{% include paper.html key="maystre2017just" %}

[1]: http://www.gif.gf/
[2]: http://www.gif.gf/about
[3]: https://s3-eu-west-1.amazonaws.com/lum-public/gifgif-dataset-20150121-v1.csv.gz
[4]: https://s3-eu-west-1.amazonaws.com/lum-public/gifgif-images-v1.tar
[5]: https://github.com/lucasmaystre/choix/blob/master/notebooks/gifgif-dataset.ipynb
