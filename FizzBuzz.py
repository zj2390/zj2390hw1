{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNNCPvi8m+fKyiqy/Qq6ie2",
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
        "<a href=\"https://colab.research.google.com/github/zj2390/zj2390hw1/blob/main/FizzBuzz.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "-dBoae4MZ1Ul"
      },
      "outputs": [],
      "source": [
        "def FizzBuzz(start, finish):\n",
        "    outlist = []\n",
        "    for i in range(start, finish + 1):\n",
        "        if i % 3 == 0 and i % 5 == 0:\n",
        "            outlist.append(\"fizzbuzz\")\n",
        "        elif i % 3 == 0:\n",
        "            outlist.append(\"fizz\")\n",
        "        elif i % 5 == 0:\n",
        "            outlist.append(\"buzz\")\n",
        "        else:\n",
        "            outlist.append(i)\n",
        "\n",
        "    return outlist\n",
        "\n",
        "\n",
        "result = FizzBuzz(1, 15)\n",
        "for item in result:\n",
        "    print(item)"
      ]
    }
  ]
}