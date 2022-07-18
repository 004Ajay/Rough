from turtle import st
import randCheck as rc

strt = int(input("Starting Number: "))

rc.start(strt)

ans = int(input("Your Opinon: "))

rc.getAns(ans, strt)