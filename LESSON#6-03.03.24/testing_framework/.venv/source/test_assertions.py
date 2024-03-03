import assertions
class TestAssertion:
    def test_assert_math(a):
        assert_var=assertions.Assertions(33)
        print(assert_var.equals_assert(33))
        print(assert_var.equals_assert(34))
        print(assert_var.bigger_assert(33))
        print(assert_var.bigger_assert(34))
        print(assert_var.smaller_assert(33))
        print(assert_var.smaller_assert(34))
    def test_assert_list(a):
        assert_var=assertions.Assertions([33,34,35])
        print(assert_var.contains_assert(33))
        print(assert_var.contains_assert(36))
        print(assert_var.starts_with_assert(33))
        print(assert_var.starts_with_assert(34))
        print(assert_var.ends_with_assert(35))
        print(assert_var.ends_with_assert(34))
    
        print(assert_var.equals_assert(33))
        print(assert_var.equals_assert(34))
        print(assert_var.bigger_assert(33))
        print(assert_var.bigger_assert(34))
        print(assert_var.smaller_assert(33))
        print(assert_var.smaller_assert(34))
    