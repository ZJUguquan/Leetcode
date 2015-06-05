# Intro to Statistics - Part3: Correlation Coefficients


class Correlator(object):

    @staticmethod
    def linear_correlation(seq):
        seq = [(x, y) for (x, y) in seq if type(x) in (int, float) and type(y) in (int, float)]
        n = len(seq)#; print n
        xs, ys = [_[0] for _ in seq], [_[1] for _ in seq]
        meanx, meany = sum(xs)/float(n), sum(ys)/float(n)

        numerator = sum([(xs[i]-meanx)*(ys[i]-meany) for i in range(n)])
        denominator_p1 = sum([(xs[i]-meanx)**2 for i in range(n)])
        denominator_p2 = sum([(ys[i]-meany)**2 for i in range(n)])
        denominator = denominator_p1 ** .5 * denominator_p2 ** .5
        return numerator/ denominator

    @staticmethod
    def is_correlation_causal(seq):
        return False

test = Test()
test.it("Linear")
data = [(x * 1.1, x * 0.1) for x in xrange(11)]
Correlator.linear_correlation(data)
test.assert_equals(round(Correlator.linear_correlation(data), 6), 1.0)


test.it("Inverse Linear")
data = [(x * 1.1, x * -1.0) for x in xrange(11)]
test.assert_equals(round(Correlator.linear_correlation(data), 6), -1.0)

test.it("Near Linear")
data = [(0, 0.5), (1, 0.9), (2, 1.8), (3, 3.1), (4, 4.3), (5, 5.1)]
test.assert_equals(round(Correlator.linear_correlation(data), 6), round(0.99058484241, 6))


test.it("data validation")

data = [(0, 0.5), (1, 0.9), (2, 1.8), (3, 3.1), (4, 4.3), ('5', 5.1)]
test.assert_equals(round(Correlator.linear_correlation(data), 6), round(0.99058484241, 6))
