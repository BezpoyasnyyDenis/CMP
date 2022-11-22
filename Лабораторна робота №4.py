{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "4d519164",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 5  8  9]\n",
      " [-1 -1  1]\n",
      " [-2  3  4]]\n",
      "[[ 1  7  0]\n",
      " [ 1  5 -2]\n",
      " [ 6 12  2]]\n",
      "[[ 4  1  9]\n",
      " [-2 -6  3]\n",
      " [-8 -9  2]]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np \n",
    "a = np.matrix('2 3 1; -1 1 0; 1 2 -1')  \n",
    "b = np.matrix('1 2 1; 0 1 2; 3 1 1')  \n",
    "c = a.dot(b)  \n",
    "print(c) \n",
    "d = b.dot(a)  \n",
    "print(d) \n",
    "g = c - d \n",
    "print(g) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "0c7a3f00",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 3  4 -4]\n",
      " [ 0  1  0]\n",
      " [-2  0  3]]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np \n",
    "a = np.array([[-1, 0, 2], [0, 1, 0], [1, 2, -1]]) \n",
    "power = np.linalg.matrix_power(a, 2) \n",
    "print(power) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "d506c104",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[-9 13]\n",
      " [15  4]]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np \n",
    "a = np.matrix('3 5; 6 -1') \n",
    "b = np.matrix('2 1; -3 2') \n",
    "c = a.dot(b) \n",
    "print(c) \n",
    "        \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "a291bbb2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[0 2 0]\n",
      " [3 4 5]\n",
      " [6 7 8]]\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "12.0"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import numpy as np \n",
    "a = np.matrix('0 2 0; 3 4 5; 6 7 8') \n",
    "print(a) \n",
    "np.linalg.det(a) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "fa784d44",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 1  2  3  4]\n",
      " [-2  1 -4  3]\n",
      " [ 3 -4 -1  2]\n",
      " [ 4  3 -2 -1]]\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "900.0000000000009"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import numpy as np \n",
    "a = np.matrix('1 2 3 4; -2 1 -4 3; 3 -4 -1 2; 4 3 -2 -1') \n",
    "print(a) \n",
    "np.linalg.det(a) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "d720bd41",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 0.11111111  0.22222222  0.22222222]\n",
      " [ 0.22222222  0.11111111 -0.22222222]\n",
      " [ 0.22222222 -0.22222222  0.11111111]]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np \n",
    "a = np.matrix('1 2 2; 2 1 -2; 2 -2 1') \n",
    "a_inv = np.linalg.inv(a) \n",
    "print(a_inv) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "4414faee",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n"
     ]
    }
   ],
   "source": [
    "import numpy as np \n",
    "a = np.matrix('1 2 3 4; 3 -1 2 5; 1 2 3 4; 1 3 4 5') \n",
    "rank = np.linalg.matrix_rank(a) \n",
    "print(rank) \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "4ce6d561",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "A= [[ 2 -1  1]\n",
      " [ 3  2  2]\n",
      " [ 1 -2  1]]\n",
      "B= [[ 2]\n",
      " [-2]\n",
      " [ 1]]\n",
      "[[ 1.2 -0.2 -0.8]\n",
      " [-0.2  0.2 -0.2]\n",
      " [-1.6  0.6  1.4]]\n",
      "X= [[ 2.]\n",
      " [-1.]\n",
      " [-3.]]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np \n",
    "a = np.matrix('2 -1 1; 3 2 2; 1 -2 1') \n",
    "b = np.matrix('2; -2; 1') \n",
    "print('A=', a) \n",
    "print('B=',b) \n",
    "a_inv = np.linalg.inv(a) \n",
    "print(a_inv) \n",
    "x = a_inv.dot(b) \n",
    "print('X=',x) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "656ddb4a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "A= [[ 2 -1  1]\n",
      " [ 3  2  2]\n",
      " [ 1 -2  1]]\n",
      "B= [[ 2]\n",
      " [-2]\n",
      " [ 1]]\n",
      "Детермінант матриці =  5.000000000000001\n",
      "Розв*язуємо систему\n",
      "x_m= [[ 2 -1  1]\n",
      " [-2  2  2]\n",
      " [ 1 -2  1]]\n",
      "y_m= [[ 2  2  1]\n",
      " [ 3 -2  2]\n",
      " [ 1  1  1]]\n",
      "z_m= [[ 2 -1  2]\n",
      " [ 3  2 -2]\n",
      " [ 1 -2  1]]\n",
      "X =  2.0\n",
      "Y= -1.0\n",
      "Z= -3.0\n"
     ]
    }
   ],
   "source": [
    "import numpy as np \n",
    "a = np.matrix('2 -1 1; 3 2 2; 1 -2 1') \n",
    "print('A=',a) \n",
    "b = np.matrix('2; -2; 1') \n",
    "print('B=',b) \n",
    "\n",
    "def kramer (a, b): \n",
    "    a_det = np.linalg.det(a) \n",
    "    print('Детермінант матриці = ', a_det) \n",
    "\n",
    "    if (a_det != 0): \n",
    "        print ('Розв*язуємо систему') \n",
    "\n",
    "        x_m = np.matrix(a) \n",
    "        x_m[:, 0] = b  \n",
    "        print('x_m=', x_m) \n",
    "        y_m = np.matrix(a) \n",
    "        y_m[:, 1] = b  \n",
    "        print('y_m=',y_m) \n",
    "\n",
    "        z_m = np.matrix(a) \n",
    "        z_m[:, 2] = b  \n",
    "        print('z_m=',z_m) \n",
    "\n",
    "        x = np.linalg.det(x_m) / a_det \n",
    "        y = np.linalg.det(y_m) / a_det \n",
    "        z = np.linalg.det(z_m) / a_det \n",
    "        print('X = ', round(x,5)) \n",
    "        print('Y=', round(y,5)) \n",
    "        print('Z=', round(z,5)) \n",
    "    else: \n",
    "        print('Розв*язків немає') \n",
    "kramer(a,b) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "b71a2d58",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[0 2 1]\n",
      " [0 1 2]\n",
      " [1 2 3]]\n",
      "Сума всіх елемнтів = 12\n",
      "Сума елемнтів 1 рядка = 3\n",
      "Сума елементів 2 рядка = 3\n",
      "Сума елементів 3 рядка = 6\n",
      "Доля 1 рядка = 25.0 %\n"
     ]
    }
   ],
   "source": [
    "import numpy as np \n",
    "a = np.array([[0, 2, 1], [0, 1, 2], [1, 2, 3]]) \n",
    "print(a) \n",
    "suma = np.sum(a) \n",
    "print(\"Сума всіх елемнтів =\", suma) \n",
    "suma1 = np.sum(a[0]) \n",
    "print(\"Сума елемнтів 1 рядка =\",suma1) \n",
    "suma2 = np.sum(a[1]) \n",
    "print(\"Сума елементів 2 рядка =\",suma2) \n",
    "suma3 = np.sum(a[2]) \n",
    "print(\"Сума елементів 3 рядка =\",suma3) \n",
    "portion1 = suma1 / suma * 100 \n",
    "portion2 = suma2 / suma * 100 \n",
    "portion3 = suma3 / suma * 100 \n",
    "print(\"Доля 1 рядка =\", portion1,\"%\") \n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3.10.0 64-bit",
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
   "version": "3.10.0"
  },
  "vscode": {
   "interpreter": {
    "hash": "afb734500600fd355917ca529030176ea0ca205570884b88f2f6f7d791fd3fbe"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
