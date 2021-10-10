use std::collections::HashMap;

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

pub fn is_palindrome(x: i32) -> bool {
    if x < 0 {
        false
    }

    

    true
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn two_sum_test() {
        assert_eq!(two_sum(vec![1,2,3,4], 5), [1, 2])
    }
}