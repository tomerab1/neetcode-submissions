impl Solution {
    pub fn encode(strs: Vec<String>) -> String {
        let mut encoded = String::new();
        for s in strs {
            encoded.push_str(&format!("{}:{}", s.len(), s));
        }
        encoded
    }

    pub fn decode(s: String) -> Vec<String> {
        let mut vec = vec![];
        let mut i = 0;
        let bytes = s.as_bytes();
        while i < bytes.len() {
            let colon_pos = s[i..].find(':').unwrap() + i;
            let len: usize = s[i..colon_pos].parse().unwrap();
            let start = colon_pos + 1;
            let end = start + len;
            vec.push(s[start..end].to_string());
            i = end;
        }

        vec
    }
}