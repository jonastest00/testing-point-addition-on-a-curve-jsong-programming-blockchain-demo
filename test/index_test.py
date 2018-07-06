from unittest import TestCase

class ECCTest(TestCase):

        def test_add1(self):
        # tests the following additions on curve y^2=x^3-7 over F_223:
        # (192,105) + (17,56)
        # (47,71) + (117,141)
        # (143,98) + (76,66)
        prime = 223
        a = FieldElement(0, prime)
        b = FieldElement(7, prime)

        additions = (
            # (x1, y1, x2, y2, x3, y3)
            (192, 105, 17, 56, 170, 142),
            (47, 71, 117, 141, 60, 139),
            (143, 98, 76, 66, 47, 71),
        )
        # iterate over the additions
            # Initialize points this way:
            # x1 = FieldElement(x1_raw, prime)
            # y1 = FieldElement(y1_raw, prime)
            # p1 = Point(x1, y1, a, b)
            # x2 = FieldElement(x2_raw, prime)
            # y2 = FieldElement(y2_raw, prime)
            # p2 = Point(x2, y2, a, b)
            # x3 = FieldElement(x3_raw, prime)
            # y3 = FieldElement(y3_raw, prime)
            # p3 = Point(x3, y3, a, b)
            # check that p1 + p2 == p3
        raise NotImplementedError
    #
    # def test_add1(self):
    #     # tests the following additions on curve y^2=x^3-7 over F_223:
    #     # (192,105) + (17,56)
    #     # (47,71) + (117,141)
    #     # (143,98) + (76,66)
    #     prime = 223
    #     a = FieldElement(0, prime)
    #     b = FieldElement(7, prime)
    #
    #     additions = (
    #         # (x1, y1, x2, y2, x3, y3)
    #         (192, 105, 17, 56, 170, 142),
    #         (47, 71, 117, 141, 60, 139),
    #         (143, 98, 76, 66, 47, 71),
    #     )
    #     # iterate over the additions
    #     for x1_raw, y1_raw, x2_raw, y2_raw, x3_raw, y3_raw in additions:
    #         # Initialize points this way:
    #         # x1 = FieldElement(x1_raw, prime)
    #         # y1 = FieldElement(y1_raw, prime)
    #         # p1 = Point(x1, y1, a, b)
    #         # x2 = FieldElement(x2_raw, prime)
    #         # y2 = FieldElement(y2_raw, prime)
    #         # p2 = Point(x2, y2, a, b)
    #         # x3 = FieldElement(x3_raw, prime)
    #         # y3 = FieldElement(y3_raw, prime)
    #         # p3 = Point(x3, y3, a, b)
    #         x1 = FieldElement(x1_raw, prime)
    #         y1 = FieldElement(y1_raw, prime)
    #         p1 = Point(x1, y1, a, b)
    #         x2 = FieldElement(x2_raw, prime)
    #         y2 = FieldElement(y2_raw, prime)
    #         p2 = Point(x2, y2, a, b)
    #         x3 = FieldElement(x3_raw, prime)
    #         y3 = FieldElement(y3_raw, prime)
    #         p3 = Point(x3, y3, a, b)
    #         # check that p1 + p2 == p3
    #         self.assertEqual(p1+p2, p3)
