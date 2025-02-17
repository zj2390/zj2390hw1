{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyO5BfxW/aO2jW64srhNidPa",
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
        "<a href=\"https://colab.research.google.com/github/zj2390/zj2390hw1/blob/main/BondPrice_Z.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "LZVudDzjZpwv"
      },
      "outputs": [],
      "source": [
        "def getBondPrice_Z(face, couponRate, times, yc):\n",
        "    \"\"\"\n",
        "    Calculate bond price using yield curve and time periods.\n",
        "    `times` and `yc` must be of equal length.\n",
        "    \"\"\"\n",
        "    coupon = face * couponRate\n",
        "    bondPrice = 0\n",
        "\n",
        "\n",
        "    for t, rate in zip(times, yc):\n",
        "        pv = coupon / (1 + rate) ** t\n",
        "        bondPrice += pv\n",
        "\n",
        "\n",
        "    bondPrice += face / (1 + yc[-1]) ** times[-1]\n",
        "\n",
        "    return bondPrice\n",
        "\n",
        "\n",
        "yc = [0.010, 0.015, 0.020, 0.025, 0.030]\n",
        "times = [1, 1.5, 3, 4, 7]\n",
        "face = 2000000\n",
        "couponRate = 0.04\n",
        "\n",
        "\n",
        "bond_price = getBondPrice_Z(face, couponRate, times, yc)\n",
        "print(f\"Bond Price: ${bond_price:,.2f}\")"
      ]
    }
  ]
}