{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOSr+vbYItPqr/W+jv6MdIV",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/zj2390/zj2390hw1/blob/main/BondDuration.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "wBGJBxoSZXDZ"
      },
      "outputs": [],
      "source": [
        "def getBondDuration(y, face, couponRate, m, ppy=1):\n",
        "    r = y / ppy\n",
        "    N = m * ppy\n",
        "    coupon = (face * couponRate) / ppy\n",
        "\n",
        "    bondPrice = 0\n",
        "    weightedCashFlow = 0\n",
        "\n",
        "    for t in range(1, N + 1):\n",
        "        pv = coupon / (1 + r) ** t\n",
        "        bondPrice += pv\n",
        "        weightedCashFlow += t * pv\n",
        "\n",
        "    pv_face = face / (1 + r) ** N\n",
        "    bondPrice += pv_face\n",
        "    weightedCashFlow += N * pv_face\n",
        "\n",
        "    bondDuration = weightedCashFlow / bondPrice\n",
        "    bondDuration /= ppy\n",
        "\n",
        "    return bondDuration\n",
        "\n",
        "\n",
        "y = 0.03\n",
        "face = 2000000\n",
        "couponRate = 0.04\n",
        "m = 10\n",
        "\n",
        "\n",
        "print(\"Bond Duration (ppy=1):\", getBondDuration(y, face, couponRate, m, ppy=1))\n",
        "print(\"Bond Duration (ppy=2):\", getBondDuration(y, face, couponRate, m, ppy=2))\n",
        "print(\"Bond Duration (ppy=4):\", getBondDuration(y, face, couponRate, m, ppy=4))"
      ]
    }
  ]
}