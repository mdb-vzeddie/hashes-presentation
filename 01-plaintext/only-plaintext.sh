cat ../accounts.json | jq -r '.[] | [.id, .username, .pw] | @csv'
