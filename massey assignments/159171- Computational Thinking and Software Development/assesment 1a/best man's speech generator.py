print("Cutis Liam Knows Preston")
print("16453897")
print()
print()


q=["enter your name: ","enter the grooms name: ","enter the brides name: ","Enter a number less than 10: ","Age you meet the groom: ","where did the bride and groom meet? ","how would you describe the groom?","how would you describe the bride?","name an animal: "]
ans=[]
for x in range(0,len(q)):
    ans.append(input(q[x]))


print("~"*36)
print(""" Here is your speech {0}
 Good evening everyone! For those who don't know me, I'm {0}.
 I met {1} when we were {4}. Right away, I knew he was a {6}
 kid and the perfect friend for me. He was always a hit with the
 ladies even at the young age of {4}. Then came along {2} and
 everything changed. It takes a {7} girl to tame the {8} that is
 {1}. I remember they met at high school and within the space
 of {3} minutes he was smitten! He told me way back then
 "{2} is the girl I'm going to marry" and here we are!
 Ladies and gentlemen, I ask you to raise your glasses for {2} and {1}.
 May they live happily ever after.""".format(ans[0],ans[1],ans[2],ans[3],ans[4],ans[5],ans[6],ans[7],ans[8],))
print("~"*36)