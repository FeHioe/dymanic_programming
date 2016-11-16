#LCS Problem Statement: Given two sequences, find the length of longest subsequence present in both of them. A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous. For example, “abc”, “abg”, “bdf”, “aeg”, ‘”acefg”, .. etc are subsequences of “abcdefg”. So a string of length n has 2^n different possible subsequences.

def LCS(string1, string2):
	common_sub = [[None]*(len(string2)+1)]
	
	for i in string1:
		common_sub.append([None]*(len(string2)+1))
	
	for i in range(0, len(string1)+1):
		for j in range(0, len(string2)+1):
			if j == 0 or i == 0:
				common_sub[i][j] = 0
			elif string1[i-1] == string2[j-1]:
				common_sub[i][j] = common_sub[i-1][j-1] + 1
			else:
				common_sub[i][j] = max(common_sub[i-1][j], common_sub[i][j-1])
	
	return common_sub[len(string1)][len(string2)]
			
def LCS_double(string1, string2):
	common_sub = []
	
	for i in range(0, len(string1)):
		for j in range(0, len(string2)):
			if string1[i] == string2[j]:
				common_sub.append(common_sub[len(common_sub)-1] + 1)

	return common_sub[len(common_sub)-1]
