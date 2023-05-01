use std::collections::HashMap;

///
/// https://leetcode.com/problems/two-sum/
///
pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
    let mut map: HashMap<i32, i32> = HashMap::new();
    for (i, n) in nums.iter().enumerate() {
        match map.get(n) {
            Some (&index) => return vec![index, i as i32],
            None => map.insert(target - n, i as i32)
        };
    }
    vec![]
}

///
/// https://leetcode.com/problems/palindrome-number/
///
pub fn is_palindrome(x: i32) -> bool {
    let s = x.to_string();
    let s1 = s.chars().rev().collect::<String>();
    s == s1
}

///
/// https://leetcode.com/problems/roman-to-integer/
///
pub fn roman_to_int(s: String) -> i32 {
    let map: HashMap<String, i32> = [
        ("I", 1),
        ("V", 5),
        ("X", 10),
        ("L", 50),
        ("C", 100),
        ("D", 500),
        ("M", 1000)
    ].iter().cloned().collect();

    let mut result:i32 = 0;

    for (i, c) in s.chars().enumerate() {

    }

    result
}


#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn two_sum_test() {
        assert_eq!(two_sum(vec![1,2,3,4], 5), [1, 2])
    }


    #[test]
    fn is_palindrome_test() {
        assert!(is_palindrome(-123), false);
    }
}