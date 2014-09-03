kafka-rpm
=========

Yet another kafka rpm repo.

Credit
======

I got the idea for this from https://github.com/edwardcapriolo/kafka-rpm.  He did a lot of really good work.  However, I wanted to do something a little different and use the pre-built binaries as well as make a lot of changes to use this for just creating a kafka cluster.  Our zookeeper cluster is handled by a different set of chef cookbooks.   Eventually I want to change this to build out a server using standard linux directories like /usr/bin and /usr/lib and not have everything all in /opt.  But for now, this is just what it took to get me started.

Howto
=====

Download the kafka_2.9.2-0.8.1.1.tgz from http://kafka.apache.org/downloads.html.  Then place it in your sources.  After that, a simple rpmbuild should work.
