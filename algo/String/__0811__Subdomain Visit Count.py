class Solution:

    # HashMap to count [O(n): 52%]
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        
        # Generate the count map
        domainToCount = collections.defaultdict(int)
        for data in cpdomains:
            count, originDomain = data.split(' ')
            count = int(count)
            subs = originDomain.split('.')
            subs = subs[::-1]
            domain = ""
            for idx, sub in enumerate(subs):
                if domain == "":
                    domain = sub
                else:
                    domain = sub + "." + domain
                domainToCount[domain] += count
        
        # Generate the res array based on count map
        res = []
        for domain, count in domainToCount.items():
            res.append(str(count) + " " + domain)
        return res
                