# intersection methods return new set with element comman in all sets

s1={1,2,3,4,5}
s2={1,2,6,7,8}
print(s1.intersection(s2))

#  intersection in three sets

s3={1,2,8,9,}
print(s1.intersection(s2,s3))

#python intersection operator
print(s1 & s2)

print("===========intersection opposite========")
print(s1.symmetric_difference(s2))

# intersection of empty set return empty set
s5={1,2}
s6={}
print(s5.intersection(s6))
