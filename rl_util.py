#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 16:47:24 2019

@author: SR13
"""
import random


class rl_util:
    def argmax(l):
        f = lambda i: l[i]
        return max(range(len(l)), key=f)

    def rand_vec(mu):
        rvec = []
        for a in mu:
            rvec.append(random.gauss(a, 1))
        return rvec

    def alpha_vec(k):
        for i in range(len(k)):
            k[i] = 1/(k[i]+1)
        return k

    def Q(alpha, r, q):
        return q + alpha * (r - q)

    def Q_vec(alvec, rvec, qvec):
        Qvec = []
        for i in range(len(alvec)):
            Qvec.append(rl_util.Q(alvec[i], rvec[i], qvec[i]))
        return Qvec


# greedy action


def n_armed_bandit(avec, sz=1000):
    qvec = [0 for i in range(len(avec))]
    steps = [0 for i in range(len(avec))]
    for k in range(1, sz+1):
        rvec = rl_util.rand_vec(avec)
        qvec = rl_util.Q_vec(rl_util.alpha_vec(steps), rvec, qvec)
        i = rl_util.argmax(qvec)
        steps[i] += 1
        print(qvec)


if __name__ == '__main__':
    n = int(input("Enter N for N-armed-bandit: "))
    print("Now enter n reward means: ")
    avec = []
    for i in range(1, n+1):
        avec.append(int(input("{} : ".format(i))))

    n_armed_bandit(avec)
