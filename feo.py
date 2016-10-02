import h2checker,alpnchecker

#url = 'http://www.google.co.jp/?gfe_rd=cr&ei=kw_xV--MJvPZ8AfugoGQCA'#'http://www.google.com'
url = 'http://www.facebook.com'
h2support = h2checker.excuteCheckFunc(url)
print(h2support)