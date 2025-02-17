{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyONz4PsYmeThlssh7sDR1qD",
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
        "<a href=\"https://colab.research.google.com/github/zj2390/zj2390hw1/blob/main/BondPrice.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "mADVP5vlY4mY",
        "outputId": "5e634eff-a397-49a4-960b-6b05cb824351",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Bond Price (ppy=1): 2170604.0567355165\n",
            "Bond Price (ppy=2): 2171686.387850823\n",
            "Bond Price (ppy=2): 2170604.0567355165\n"
          ]
        }
      ],
      "source": [
        "def getBondPrice(y, face, couponRate, m, ppy=1):\n",
        "    r = y / ppy\n",
        "    N = m * ppy\n",
        "    coupon = (face * couponRate) / ppy\n",
        "\n",
        "    bondPrice = 0\n",
        "    for t in range(1, N + 1):\n",
        "        bondPrice += coupon / (1 + r) ** t\n",
        "\n",
        "    bondPrice += face / (1 + r) ** N\n",
        "\n",
        "    return bondPrice\n",
        "\n",
        "\n",
        "y = 0.03\n",
        "face = 2000000\n",
        "couponRate = 0.04\n",
        "m = 10\n",
        "\n",
        "\n",
        "print(\"Bond Price (ppy=1):\", getBondPrice(y, face, couponRate, m, ppy=1))\n",
        "print(\"Bond Price (ppy=2):\", getBondPrice(y, face, couponRate, m, ppy=2))\n",
        "print(\"Bond Price (ppy=2):\", getBondPrice(y, face, couponRate, m))"
      ]
    }
  ]
}