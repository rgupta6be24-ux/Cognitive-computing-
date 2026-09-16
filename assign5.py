{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "a0abfbdf",
   "metadata": {},
   "source": [
    "Q.1 Write a program to create a NumPy 1D-array with 5 elements and perform basic\n",
    "operations like:\n",
    "a) Addition of 2 in all the element\n",
    "b) Multiply 3 with all the elements\n",
    "c) Divide every element by 2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "26c0c244",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[10 11 12 13 14]\n",
      "[12 13 14 15 16]\n",
      "[30 33 36 39 42]\n",
      "[5.  5.5 6.  6.5 7. ]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "array = np.array([10,11,12,13,14])\n",
    "print(array)\n",
    "print(array+2)\n",
    "print(array*3)\n",
    "print(array/2)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "46660190",
   "metadata": {},
   "source": [
    "Q.2 Questions on Basic NumPy Array:\n",
    "a) Reverse the NumPy array: arr = np.array([1, 2, 3, 6, 4, 5])\n",
    "b) Find the most frequent value and their indice(s) in the following arrays:\n",
    "i. x = np.array([1,2,3,4,5,1,2,1,1,1])\n",
    "ii. y = np.array([1, 1, 1, 2, 3, 4, 2, 4, 3, 3, ])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "a5232ab5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[5 4 6 3 2 1]\n"
     ]
    }
   ],
   "source": [
    "array = np.array([1, 2, 3, 6, 4, 5])\n",
    "reversed_array = array[::-1]\n",
    "print(reversed_array)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "5b8cd6c5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "[0 5 7 8 9]\n",
      "1\n",
      "[0 1 2]\n"
     ]
    }
   ],
   "source": [
    "x = np.array([1,2,3,4,5,1,2,1,1,1])\n",
    "y = np.array([1, 1, 1, 2, 3, 4, 2, 4, 3, 3, ])\n",
    "\n",
    "most_freq_vals = np.argmax(np.bincount(x))\n",
    "indices = np.where(x == most_freq_vals)[0]\n",
    "print(most_freq_vals)\n",
    "print(indices)\n",
    "\n",
    "most_freq_vals = np.argmax(np.bincount(y))\n",
    "indices = np.where(y == most_freq_vals)[0]\n",
    "print(most_freq_vals)\n",
    "print(indices)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0b5e0695",
   "metadata": {},
   "source": [
    "Q.3 For the given 2-D array arr=np.array([10, 20, 30], [40, 50, 60], [70, 80, 90]), access\n",
    "elements using row and column indices as follows:\n",
    "a) Access 1st row, 2nd column\n",
    "b) Access 3rd row, 1st column"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "9049d1f9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "20\n",
      "70\n"
     ]
    }
   ],
   "source": [
    "arr  = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])\n",
    "print(arr[0,1])\n",
    "print(arr[2,0])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f2167401",
   "metadata": {},
   "source": [
    "Q.4 Write program to create an 1-D NumPy array named <<Your Name>> with evenly\n",
    "spaced 25 numbers from 10 to 100 using linspace(). Print the dimensions of the array,\n",
    "shape, total elements, the data type of each element and total number of bytes consumed\n",
    "by the array. Find the transpose of this array using reshape() attribute. Can we do the same\n",
    "with T attribute?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "cb9cd5eb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Array:\n",
      "[ 10.    13.75  17.5   21.25  25.    28.75  32.5   36.25  40.    43.75\n",
      "  47.5   51.25  55.    58.75  62.5   66.25  70.    73.75  77.5   81.25\n",
      "  85.    88.75  92.5   96.25 100.  ]\n",
      "\n",
      "Dimensions: 1\n",
      "Shape: (25,)\n",
      "Total elements: 25\n",
      "Data type: float64\n",
      "Total bytes consumed: 200\n",
      "\n",
      "Transpose using reshape():\n",
      "[[ 10.  ]\n",
      " [ 13.75]\n",
      " [ 17.5 ]\n",
      " [ 21.25]\n",
      " [ 25.  ]\n",
      " [ 28.75]\n",
      " [ 32.5 ]\n",
      " [ 36.25]\n",
      " [ 40.  ]\n",
      " [ 43.75]\n",
      " [ 47.5 ]\n",
      " [ 51.25]\n",
      " [ 55.  ]\n",
      " [ 58.75]\n",
      " [ 62.5 ]\n",
      " [ 66.25]\n",
      " [ 70.  ]\n",
      " [ 73.75]\n",
      " [ 77.5 ]\n",
      " [ 81.25]\n",
      " [ 85.  ]\n",
      " [ 88.75]\n",
      " [ 92.5 ]\n",
      " [ 96.25]\n",
      " [100.  ]]\n",
      "\n",
      "Transpose using T:\n",
      "[ 10.    13.75  17.5   21.25  25.    28.75  32.5   36.25  40.    43.75\n",
      "  47.5   51.25  55.    58.75  62.5   66.25  70.    73.75  77.5   81.25\n",
      "  85.    88.75  92.5   96.25 100.  ]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "\n",
    "rishi" = np.linspace(10, 100, 25)\n",
    "\n",
    "print(\"Array:\")\n",
    "print(rishi)\n",
    "\n",
    "print(\"\\nDimensions:\", rishi.ndim)\n",
    "print(\"Shape:\", rishi.shape)\n",
    "print(\"Total elements:\", rishi.size)\n",
    "print(\"Data type:\", rishi.dtype)\n",
    "print(\"Total bytes consumed:\", rishi.nbytes)\n",
    "\n",
    "transpose = rishi.reshape(25, 1)\n",
    "print(\"\\nTranspose using reshape():\")\n",
    "print(transpose)\n",
    "\n",
    "print(\"\\nTranspose using T:\")\n",
    "print(rishi.T)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c10503fe",
   "metadata": {},
   "source": [
    "Q5. Create a 2-D Array of three rows and four columns, named ucs420_<your_name>>\n",
    "with following values – 10, 20, 30, 40, 50, 60, 70, 80, 90, 15, 20, 35. Compute the mean,\n",
    "median, max, min, unique elements. Reshape the array to four rows and three columns and\n",
    "name it as reshaped_ ucs420_<your_name>>. Resize the array to two rows and three\n",
    "columns and name it as resized_ ucs420_<your_name>>."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "83c704f3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Original Array:\n",
      "[[10 20 30 40]\n",
      " [50 60 70 80]\n",
      " [90 15 20 35]]\n",
      "\n",
      "Mean: 43.333333333333336\n",
      "Median: 37.5\n",
      "Maximum: 90\n",
      "Minimum: 10\n",
      "Unique Elements: [10 15 20 30 35 40 50 60 70 80 90]\n",
      "\n",
      "Reshaped Array (4 x 3):\n",
      "[[10 20 30]\n",
      " [40 50 60]\n",
      " [70 80 90]\n",
      " [15 20 35]]\n",
      "\n",
      "Resized Array (2 x 3):\n",
      "[[10 20 30]\n",
      " [40 50 60]]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "\n",
    "ucs420_rishi = np.array([\n",
    "    [10, 20, 30, 40],\n",
    "    [50, 60, 70, 80],\n",
    "    [90, 15, 20, 35]\n",
    "])\n",
    "\n",
    "print(\"Original Array:\")\n",
    "print(ucs420_rishi)\n",
    "\n",
    "print(\"\\nMean:\", np.mean(ucs420_rishi))\n",
    "print(\"Median:\", np.median(ucs420_rishi))\n",
    "print(\"Maximum:\", np.max(ucs420_rishi))\n",
    "print(\"Minimum:\", np.min(ucs420_rishi))\n",
    "print(\"Unique Elements:\", np.unique(ucs420_rishi))\n",
    "\n",
    "reshaped_ucs420_rishi = ucs420_rishi.reshape(4, 3)\n",
    "\n",
    "print(\"\\nReshaped Array (4 x 3):\")\n",
    "print(reshaped_ucs420_rishi)\n",
    "\n",
    "resized_ucs420_rishi = np.resize(ucs420_rishi, (2, 3))\n",
    "\n",
    "print(\"\\nResized Array (2 x 3):\")\n",
    "print(resized_ucs420_rishi)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
