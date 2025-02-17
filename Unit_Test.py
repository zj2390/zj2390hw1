{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyM6Y/oVWh2Svd8Woz7nZn2T",
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
        "<a href=\"https://colab.research.google.com/github/zj2390/zj2390hw1/blob/main/Unit_Test.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Unit_Test"
      ],
      "metadata": {
        "id": "iPNKhu8IhooO"
      }
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "NkvKCRcWhe9v"
      },
      "outputs": [],
      "source": [
        "import whoami\n",
        "def test_WhoAmI():\n",
        "    assert whoami.WhoAmI() != 'djr2132'\n",
        "\n",
        "import bondprice\n",
        "def test_getBondPrice():\n",
        "    assert round(bondprice.getBondPrice(.03, 2000000, .04, 10,  1)) == 2170604\n",
        "    assert round(bondprice.getBondPrice(.03, 2000000, .04, 10,  2)) == 2171686\n",
        "\n",
        "import bondduration\n",
        "def test_getBondDuration():\n",
        "    assert round(bondduration.getBondDuration(.03, 2000000, .04, 10,1),2) == 8.51\n",
        "\n",
        "import bondprice_e\n",
        "def test_GetBondPriceE():\n",
        "    yc = [.010,.015,.020,.025,.030]\n",
        "    face = 2000000\n",
        "    couponRate = .04\n",
        "    m=5\n",
        "    assert round(bondprice_e.getBondPrice_E(face, couponRate,m, yc)) == 2098949\n",
        "\n",
        "import bondprice_z\n",
        "def test_GetBondPriceZ():\n",
        "    yc = [.010,.015,.020,.025,.030]\n",
        "    times=[1,1.5,3,4,7]\n",
        "    face = 2000000\n",
        "    couponRate = .04\n",
        "    x = bondprice_z.getBondPrice_Z(face, couponRate, times, yc)\n",
        "    assert round(x) == 1996533\n",
        "\n",
        "import fizzbuzz\n",
        "def test_FizzBuzz():\n",
        "    x = fizzbuzz.FizzBuzz(40,45)\n",
        "    assert x[0] == \"buzz\"\n",
        "    assert x[1] == 41\n",
        "    assert x[5] == \"fizzbuzz\"\n"
      ]
    }
  ]
}