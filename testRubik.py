import unittest
from RubikCube import RubikCube
import numpy

class Test_testRubik(unittest.TestCase):

    def test_MoveRight(self):
        r = RubikCube()
        rFinal = RubikCube()
        r.initColor()
        rFinal.initColor()

        r.rotateRight()
        r.rotateRight()
        r.rotateRight()
        r.rotateRight()

        assert(r==rFinal)

    def test_MoveRightInverse(self):
        r = RubikCube()
        rFinal = RubikCube()
        r.initColor()
        rFinal.initColor()

        r.rotateRightInverse()
        r.rotateRightInverse()
        r.rotateRightInverse()
        r.rotateRightInverse()

        assert(r==rFinal)


    def test_MoveLeft(self):
        r = RubikCube()
        rFinal = RubikCube()
        r.initColor()
        rFinal.initColor()

        r.rotateLeft()
        r.rotateLeft()
        r.rotateLeft()
        r.rotateLeft()

        assert(r==rFinal)

    def test_MoveLeftInverse(self):
        r = RubikCube()
        rFinal = RubikCube()
        r.initColor()
        rFinal.initColor()

        r.rotateLeftInverse()
        r.rotateLeftInverse()
        r.rotateLeftInverse()
        r.rotateLeftInverse()

        assert(r==rFinal)

    def test_MoveFront(self):
        r = RubikCube()
        rFinal = RubikCube()
        r.initColor()
        rFinal.initColor()

        r.rotateFront()
        r.rotateFront()
        r.rotateFront()
        r.rotateFront()

        assert(r==rFinal)

    def test_MoveFrontInverse(self):
        r = RubikCube()
        rFinal = RubikCube()
        r.initColor()
        rFinal.initColor()

        r.rotateFrontInverse()
        r.rotateFrontInverse()
        r.rotateFrontInverse()
        r.rotateFrontInverse()

        assert(r==rFinal)

    def test_MoveBack(self):
        r = RubikCube()
        rFinal = RubikCube()
        r.initColor()
        rFinal.initColor()

        r.rotateBack()
        r.rotateBack()
        r.rotateBack()
        r.rotateBack()

        assert(r==rFinal)

    def test_MoveBackInverse(self):
        r = RubikCube()
        rFinal = RubikCube()
        r.initColor()
        rFinal.initColor()

        r.rotateBackInverse()
        r.rotateBackInverse()
        r.rotateBackInverse()
        r.rotateBackInverse()

        assert(r==rFinal)

    def test_MoveDown(self):
        r = RubikCube()
        rFinal = RubikCube()
        r.initColor()
        rFinal.initColor()

        r.rotateBack()
        r.rotateBack()
        r.rotateBack()
        r.rotateBack()

        assert(r==rFinal)

    def test_MoveDownInverse(self):
        r = RubikCube()
        rFinal = RubikCube()
        r.initColor()
        rFinal.initColor()

        r.rotateDownInverse()
        r.rotateDownInverse()
        r.rotateDownInverse()
        r.rotateDownInverse()

        assert(r==rFinal)

    def test_MoveUp(self):
        r = RubikCube()
        rFinal = RubikCube()
        r.initColor()
        rFinal.initColor()

        r.rotateUp()
        r.rotateUp()
        r.rotateUp()
        r.rotateUp()

        assert(r==rFinal)

    def test_MoveUpInverse(self):
        r = RubikCube()
        rFinal = RubikCube()
        r.initColor()
        rFinal.initColor()

        r.rotateUpInverse()
        r.rotateUpInverse()
        r.rotateUpInverse()
        r.rotateUpInverse()

        assert(r==rFinal)

if __name__ == '__main__':
    unittest.main()
