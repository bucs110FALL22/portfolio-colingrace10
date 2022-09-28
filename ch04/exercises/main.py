football = ("Despite being one of the best running backs to come out of college in years, Najee Harris, who got selected in the first round of the 2021 NFL Draft by the Pittsburgh Steelers, has not forgotten his roots. He and his four siblings were raised by a single mother who struggled to make ends meet, and they spent time at several homeless shelters throughout his childhood.He helped renovate one of the shelters during the Steelers Bye Week and is a great role model for anyone who feels stranded in a similarly unfortunate situation, as he stayed strong and wound up reaching his dream of playing in the NFL. The versatile wrecking ball has proven to be an even better person off the field than he is a player on it, and that is saying something considering he already looks like one of the league's best running backs. Terrell Owens did not have an easy home life growing up, as his father was absent, and his mother had to work tirelessly to put food on the table for the family. He also dealt with abandonment issues after learning that his father started a new family despite living across the street from him. Sports became an outlet for Owens in high school, as he displayed rare athletic ability and eventually earned a scholarship at the University of Tennessee-Chattanooga, where he thrived in basketball and football. He was later selected in the third round of the 1996 NFL Draft by the San Francisco 49ers and had one of the most prolific careers of any receiver in league history.")


dict = {
  "nfl" : "No Fun League", 
  "football" : "Pig skin", 
  "league" : "world"}

for key, value in dict.items():
  article = football.replace(key, value)
print(article)