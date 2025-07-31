class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        parents = list(range(n))

        def find(x) :
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]
        
        def union(x,y):
            px,py = find(x), find(y)
            if px!= py:
                parents[py] = px
        
        email_id = {}

        for i ,acct in enumerate(accounts):
            for email in acct[1:]:
                if email in email_id:
                    union(i,email_id[email])
                else:
                    email_id[email] = i
        

        mp = defaultdict(set)
        for email, idx in email_id.items():
            root = find(idx)
            mp[root].add(email)
        
        ans = []
        for root, emails in mp.items():
            name = accounts[root][0]
            ans.append([name] + sorted(emails))
        return ans
            

        return result