{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNbQYQyp2stovzAz3Kgj398",
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
        "<a href=\"https://colab.research.google.com/github/zj2390/zj2390hw1/blob/main/BondPrice_E.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "rLdzMHqyZiZd"
      },
      "outputs": [],
      "source": [
        "def getBondPrice_E(face, couponRate, m, yc):\n",
        "    \"\"\"\n",
        "    Calculate bond price using a yield curve (yc).\n",
        "    yc is a list where each element represents the yield for that period.\n",
        "    \"\"\"\n",
        "    coupon = face * couponRate\n",
        "    bondPrice = 0\n",
        "\n",
        "\n",
        "    for t, rate in enumerate(yc, start=1):\n",
        "        pv = coupon / (1 + rate) ** t\n",
        "        bondPrice += pv\n",
        "\n",
        "\n",
        "    bondPrice += face / (1 + yc[-1]) ** m\n",
        "\n",
        "    return bondPrice\n",
        "\n",
        "\n",
        "yc = [0.010, 0.015, 0.020, 0.025, 0.030]\n",
        "face = 2000000\n",
        "couponRate = 0.04\n",
        "m = 5\n",
        "\n",
        "\n",
        "bond_price = getBondPrice_E(face, couponRate, m, yc)\n",
        "print(f\"Bond Price: ${bond_price:,.2f}\")"
      ]
    }
  ]
}