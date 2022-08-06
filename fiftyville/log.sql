-- Keep a log of any SQL queries you execute as you solve the mystery.

The CS50 Duck has been stolen! The town of Fiftyville has called upon you
to solve the mystery of the stolen duck. Authorities believe that
the thief stole the duck and then, shortly afterwards,
took a flight out of town with the help of an accomplice.

Your goal is to identify:

Who the thief is,
What city the thief escaped to, and
Who the thief’s accomplice is who helped them escape
All you know is that the theft took place on July 28, 2021 and that it took place on Humphrey Street.

SELECT * FROM crime_scene_reports WHERE description LIKE '%duck%';
+-----+------+-------+-----+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| id  | year | month | day |     street      |                                                                                                       description                                                                                                        |
+-----+------+-------+-----+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 295 | 2021 | 7     | 28  | Humphrey Street | Theft of the CS50 duck took place at 10:15am
 at the Humphrey Street bakery.
 Interviews were conducted today with three witnesses who were present at the time –
 each of their interview transcripts mentions the bakery. |
+-----+------+-------+-----+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


sqlite> SELECT * FROM interviews WHERE transcript LIKE "%bakery%";
+-----+---------+------+-------+-----+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| id  |  name   | year | month | day |                                                                                                                                                     transcript                                                                                                                                                      |
+-----+---------+------+-------+-----+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 161 | Ruth    | 2021 | 7     | 28  |
Sometime within ten minutes of the theft,
I saw the thief get into a car in the bakery parking lot and drive away.
If you have security footage from the bakery parking lot, you might want
to look for cars that left the parking lot in that time frame.  --> watch the security cameras
                                                       |
| 162 | Eugene  | 2021 | 7     | 28  |
I don't know the thief's name, but it was someone I recognized.
Earlier this morning, before I arrived at Emmas bakery,
I was walking by the ATM on Leggett Street
and saw the thief there withdrawing some money. --> look for withdrawals at Legett Street on the date
                                                                                               |
| 163 | Raymond | 2021 | 7     | 28  |
As the thief was leaving the bakery,
they called someone who talked to them for less than a minute.
In the call, I heard the thief say that --> check phone calls at that time
they were planning to take the earliest flight out of Fiftyville tomorrow. --> check flights on the next day
 The thief then asked the person on the other end of the phone to purchase the flight ticket.
 --> conscript bought a ticket for the erliest flight on 29

| 192 | Kiana   | 2021 | 5     | 17  |
I saw Richard take a bite out of his pastry at the bakery before his pastry was stolen from him.                                                                                                                                                                                                                    |
+-----+---------+------+-------+-----+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

SELECT * FROM bakery_security_logs WHERE year = 2021 AND month = 7 AND day = 28 AND hour < 11 AND activity = "exit";
+-----+------+-------+-----+------+--------+----------+---------------+
| id  | year | month | day | hour | minute | activity | license_plate |
+-----+------+-------+-----+------+--------+----------+---------------+
| 219 | 2021 | 7     | 28  | 8    | 2      | entrance | 1M92998       |
| 220 | 2021 | 7     | 28  | 8    | 2      | entrance | N507616       |
| 221 | 2021 | 7     | 28  | 8    | 2      | exit     | 1M92998       |
| 222 | 2021 | 7     | 28  | 8    | 2      | exit     | N507616       |
| 223 | 2021 | 7     | 28  | 8    | 7      | entrance | 7Z8B130       |
| 224 | 2021 | 7     | 28  | 8    | 7      | exit     | 7Z8B130       |
| 225 | 2021 | 7     | 28  | 8    | 13     | entrance | 47MEFVA       |
| 226 | 2021 | 7     | 28  | 8    | 13     | exit     | 47MEFVA       |
| 227 | 2021 | 7     | 28  | 8    | 15     | entrance | D965M59       |
| 228 | 2021 | 7     | 28  | 8    | 15     | entrance | HW0488P       |
| 229 | 2021 | 7     | 28  | 8    | 15     | exit     | D965M59       |
| 230 | 2021 | 7     | 28  | 8    | 15     | exit     | HW0488P       |
| 231 | 2021 | 7     | 28  | 8    | 18     | entrance | L93JTIZ       |
| 232 | 2021 | 7     | 28  | 8    | 23     | entrance | 94KL13X       |
| 233 | 2021 | 7     | 28  | 8    | 25     | entrance | L68E5I0       |
| 234 | 2021 | 7     | 28  | 8    | 25     | entrance | HOD8639       |
| 235 | 2021 | 7     | 28  | 8    | 25     | exit     | HOD8639       |
| 236 | 2021 | 7     | 28  | 8    | 34     | exit     | L68E5I0       |
| 237 | 2021 | 7     | 28  | 8    | 34     | entrance | 1106N58       |
| 238 | 2021 | 7     | 28  | 8    | 34     | entrance | W2CT78U       |
| 239 | 2021 | 7     | 28  | 8    | 34     | exit     | W2CT78U       |
| 240 | 2021 | 7     | 28  | 8    | 36     | entrance | 322W7JE       |
| 241 | 2021 | 7     | 28  | 8    | 38     | entrance | 3933NUH       |
| 242 | 2021 | 7     | 28  | 8    | 38     | exit     | 3933NUH       |
| 243 | 2021 | 7     | 28  | 8    | 42     | entrance | 0NTHK55       |
| 244 | 2021 | 7     | 28  | 8    | 44     | entrance | 1FBL6TH       |
| 245 | 2021 | 7     | 28  | 8    | 44     | exit     | 1FBL6TH       |
| 246 | 2021 | 7     | 28  | 8    | 49     | entrance | P14PE2Q       |
| 247 | 2021 | 7     | 28  | 8    | 49     | exit     | P14PE2Q       |
| 248 | 2021 | 7     | 28  | 8    | 50     | entrance | 4V16VO0       |
| 249 | 2021 | 7     | 28  | 8    | 50     | exit     | 4V16VO0       |
| 250 | 2021 | 7     | 28  | 8    | 57     | entrance | 8LLB02B       |
| 251 | 2021 | 7     | 28  | 8    | 57     | exit     | 8LLB02B       |
| 252 | 2021 | 7     | 28  | 8    | 59     | entrance | O784M2U       |
| 253 | 2021 | 7     | 28  | 8    | 59     | exit     | O784M2U       |
| 254 | 2021 | 7     | 28  | 9    | 14     | entrance | 4328GD8       |
| 255 | 2021 | 7     | 28  | 9    | 15     | entrance | 5P2BI95       |
| 256 | 2021 | 7     | 28  | 9    | 20     | entrance | 6P58WS2       |
| 257 | 2021 | 7     | 28  | 9    | 28     | entrance | G412CB7       |
| 258 | 2021 | 7     | 28  | 10   | 8      | entrance | R3G7486       |
| 259 | 2021 | 7     | 28  | 10   | 14     | entrance | 13FNH73       |
| 260 | 2021 | 7     | 28  | 10   | 16     | exit     | 5P2BI95       | --> 10:15 crime occured
| 261 | 2021 | 7     | 28  | 10   | 18     | exit     | 94KL13X       | --> suspect 1
| 262 | 2021 | 7     | 28  | 10   | 18     | exit     | 6P58WS2       |
| 263 | 2021 | 7     | 28  | 10   | 19     | exit     | 4328GD8       |
| 264 | 2021 | 7     | 28  | 10   | 20     | exit     | G412CB7       |
| 265 | 2021 | 7     | 28  | 10   | 21     | exit     | L93JTIZ       |
| 266 | 2021 | 7     | 28  | 10   | 23     | exit     | 322W7JE       |
| 267 | 2021 | 7     | 28  | 10   | 23     | exit     | 0NTHK55       |
| 268 | 2021 | 7     | 28  | 10   | 35     | exit     | 1106N58       | --> one of this cars has exited
| 269 | 2021 | 7     | 28  | 10   | 42     | entrance | NRYN856       |
| 270 | 2021 | 7     | 28  | 10   | 44     | entrance | WD5M8I6       |
| 271 | 2021 | 7     | 28  | 10   | 55     | entrance | V47T75I       |
+-----+------+-------+-----+------+--------+----------+---------------+

SELECT * FROM atm_transactions WHERE atm_location LIKE '%Leggett%' AND transaction_type = "withdraw" AND day = 28;
+-----+----------------+------+-------+-----+----------------+------------------+--------+
| id  | account_number | year | month | day |  atm_location  | transaction_type | amount |
+-----+----------------+------+-------+-----+----------------+------------------+--------+
| 246 | 28500762       | 2021 | 7     | 28  | Leggett Street | withdraw         | 48     |
| 264 | 28296815       | 2021 | 7     | 28  | Leggett Street | withdraw         | 20     |
| 266 | 76054385       | 2021 | 7     | 28  | Leggett Street | withdraw         | 60     |
| 267 | 49610011       | 2021 | 7     | 28  | Leggett Street | withdraw         | 50     |
| 269 | 16153065       | 2021 | 7     | 28  | Leggett Street | withdraw         | 80     |
| 288 | 25506511       | 2021 | 7     | 28  | Leggett Street | withdraw         | 20     |
| 313 | 81061156       | 2021 | 7     | 28  | Leggett Street | withdraw         | 30     |
| 336 | 26013199       | 2021 | 7     | 28  | Leggett Street | withdraw         | 35     |
+-----+----------------+------+-------+-----+----------------+------------------+--------+
--> check same bank account for suspitious activities.
--> Might intersect with bank accounts of the ppl who bought tickets that day

SELECT * FROM flights WHERE day = 29 ORDER BY hour;
+----+-------------------+------------------------+------+-------+-----+------+--------+
| id | origin_airport_id | destination_airport_id | year | month | day | hour | minute |
+----+-------------------+------------------------+------+-------+-----+------+--------+
| 36 | 8                 | 4                      | 2021 | 7     | 29  | 8    | 20     | --> that flight 36
| 43 | 8                 | 1                      | 2021 | 7     | 29  | 9    | 30     |
| 23 | 8                 | 11                     | 2021 | 7     | 29  | 12   | 15     |
| 53 | 8                 | 9                      | 2021 | 7     | 29  | 15   | 20     |
| 18 | 8                 | 6                      | 2021 | 7     | 29  | 16   | 0      |
+----+-------------------+------------------------+------+-------+-----+------+--------+

SELECT * FROM airports WHERE id = 8;
+----+--------------+-----------------------------+------------+
| id | abbreviation |          full_name          |    city    |
+----+--------------+-----------------------------+------------+
| 8  | CSF          | Fiftyville Regional Airport | Fiftyville | --> origin airport
+----+--------------+-----------------------------+------------+

SELECT * FROM airports WHERE id = 4;
+----+--------------+-------------------+---------------+
| id | abbreviation |     full_name     |     city      |
+----+--------------+-------------------+---------------+
| 4  | LGA          | LaGuardia Airport | New York City | --> destination
+----+--------------+-------------------+---------------+

SELECT * FROM phone_calls WHERE day = 28 AND duration < 60;
+-----+----------------+----------------+------+-------+-----+----------+
| id  |     caller     |    receiver    | year | month | day | duration | --> thief called to ask to book a ticket
+-----+----------------+----------------+------+-------+-----+----------+
| 221 | (130) 555-0289 | (996) 555-8899 | 2021 | 7     | 28  | 51       | -- suspect 3
| 224 | (499) 555-9472 | (892) 555-8872 | 2021 | 7     | 28  | 36       | -- suspect 4
| 233 | (367) 555-5533 | (375) 555-8161 | 2021 | 7     | 28  | 45       | -- suspect 1
| 251 | (499) 555-9472 | (717) 555-1342 | 2021 | 7     | 28  | 50       | -- suspect 4
| 254 | (286) 555-6063 | (676) 555-6554 | 2021 | 7     | 28  | 43       | -- suspect 5
| 255 | (770) 555-1861 | (725) 555-3243 | 2021 | 7     | 28  | 49       |
| 261 | (031) 555-6622 | (910) 555-3251 | 2021 | 7     | 28  | 38       |
| 279 | (826) 555-1652 | (066) 555-9701 | 2021 | 7     | 28  | 55       |
| 281 | (338) 555-6650 | (704) 555-2131 | 2021 | 7     | 28  | 54       |
+-----+----------------+----------------+------+-------+-----+----------+

SELECT * FROM passengers WHERE flight_id = 36;
+-----------+-----------------+------+
| flight_id | passport_number | seat | --> one of this passengers is a thief
+-----------+-----------------+------+
| 36        | 7214083635      | 2A   |
| 36        | 1695452385      | 3B   |
| 36        | 5773159633      | 4A   |
| 36        | 1540955065      | 5C   |
| 36        | 8294398571      | 6C   |
| 36        | 1988161715      | 6D   |
| 36        | 9878712108      | 7A   |
| 36        | 8496433585      | 7B   |
+-----------+-----------------+------+

SELECT * FROM people WHERE passport_number IN (SELECT passport_number  FROM passengers WHERE flight_id = 36);
+--------+--------+----------------+-----------------+---------------+
|   id   |  name  |  phone_number  | passport_number | license_plate | --> one of this people is a thief
+--------+--------+----------------+-----------------+---------------+
| 395717 | Kenny  | (826) 555-1652 | 9878712108      | 30G67EN       |
| 398010 | Sofia  | (130) 555-0289 | 1695452385      | G412CB7       | --> suspect 3
| 449774 | Taylor | (286) 555-6063 | 1988161715      | 1106N58       | --> suspect 5
| 467400 | Luca   | (389) 555-5198 | 8496433585      | 4328GD8       | --> suspect 2
| 560886 | Kelsey | (499) 555-9472 | 8294398571      | 0NTHK55       | --> suspect 4
| 651714 | Edward | (328) 555-1152 | 1540955065      | 130LD9Z       |
| 686048 | Bruce  | (367) 555-5533 | 5773159633      | 94KL13X       | --> suspect 1
| 953679 | Doris  | (066) 555-9701 | 7214083635      | M51FA04       |
+--------+--------+----------------+-----------------+---------------+

--> too many suspects, we need to run queries to make sure

SELECT * FROM people WHERE passport_number IN (SELECT passport_number  FROM passengers WHERE flight_id = 36);

SELECT * FROM bakery_security_logs WHERE license_plate IN (
    SELECT license_plate FROM people WHERE passport_number IN (
        SELECT passport_number  FROM passengers WHERE flight_id = 36);

SELECT * FROM bakery_security_logs WHERE license_plate IN
    (SELECT license_plate FROM people WHERE passport_number IN
        (SELECT passport_number  FROM passengers WHERE flight_id = 36))
AND year = 2021 AND month = 7 AND day = 28 AND hour < 11 AND activity = "exit";

+-----+------+-------+-----+------+--------+----------+---------------+
| id  | year | month | day | hour | minute | activity | license_plate |
+-----+------+-------+-----+------+--------+----------+---------------+
| 261 | 2021 | 7     | 28  | 10   | 18     | exit     | 94KL13X       |
| 263 | 2021 | 7     | 28  | 10   | 19     | exit     | 4328GD8       |
| 264 | 2021 | 7     | 28  | 10   | 20     | exit     | G412CB7       |
| 267 | 2021 | 7     | 28  | 10   | 23     | exit     | 0NTHK55       |
| 268 | 2021 | 7     | 28  | 10   | 35     | exit     | 1106N58       |
+-----+------+-------+-----+------+--------+----------+---------------+

SELECT license_plate FROM bakery_security_logs WHERE license_plate IN
    (SELECT license_plate FROM people WHERE passport_number IN
        (SELECT passport_number  FROM passengers WHERE flight_id = 36))
AND year = 2021 AND month = 7 AND day = 28 AND hour < 11 AND activity = "exit";

SELECT * FROM bakery_security_logs WHERE license_plate IN
    (SELECT license_plate FROM bakery_security_logs WHERE license_plate IN
        (SELECT license_plate FROM people WHERE passport_number IN
            (SELECT passport_number  FROM passengers WHERE flight_id = 36))
                AND year = 2021 AND month = 7 AND day = 28 AND hour < 11 AND activity = "exit")
AND year = 2021 AND month = 7 AND day = 28 AND hour < 11 AND hour < 10 AND activity = "exit";

| 686048 | Bruce  | (367) 555-5533 | 5773159633      | 94KL13X       | --> suspect 1
--| 467400 | Luca   | (389) 555-5198 | 8496433585      | 4328GD8       | --> suspect 2 didnt call anyone
| 398010 | Sofia  | (130) 555-0289 | 1695452385      | G412CB7       | --> suspect 3
| 560886 | Kelsey | (499) 555-9472 | 8294398571      | 0NTHK55       | --> suspect 4
| 449774 | Taylor | (286) 555-6063 | 1988161715      | 1106N58       | --> suspect 5

| 233 | (367) 555-5533 | (375) 555-8161 | 2021 | 7     | 28  | 45       | -- suspect 1
| 221 | (130) 555-0289 | (996) 555-8899 | 2021 | 7     | 28  | 51       | -- suspect 3
| 224 | (499) 555-9472 | (892) 555-8872 | 2021 | 7     | 28  | 36       | -- suspect 4
| 251 | (499) 555-9472 | (717) 555-1342 | 2021 | 7     | 28  | 50       | -- suspect 4
| 254 | (286) 555-6063 | (676) 555-6554 | 2021 | 7     | 28  | 43       | -- suspect 5

--check phones they have been calling

-- coinscript search
SELECT * from people WHERE phone_number LIKE '%8161%'; --1
SELECT * from people WHERE phone_number LIKE '%8899%'; --2
SELECT * from people WHERE phone_number LIKE '%8872%'; --4
SELECT * from people WHERE phone_number LIKE '%1342%'; --4
SELECT * from people WHERE phone_number LIKE '%6554%'; --5

OR LIKE '%8899%' OR LIKE '%8872%' OR LIKE '%1342%' OR LIKE '%6554%';

-- this is list of people who suspects called under a minute at that time to ask to order a ticket

+--------+-------+----------------+-----------------+---------------+
|   id   | name  |  phone_number  | passport_number | license_plate |
+--------+-------+----------------+-----------------+---------------+
| 864400 | Robin | (375) 555-8161 |                 | 4V16VO0       | --1
+--------+-------+----------------+-----------------+---------------+
| 567218 | Jack | (996) 555-8899 | 9029462229      | 52R0Y8U       | --2.0.0 -- has a bank account
+--------+------+----------------+-----------------+---------------+
| 251693 | Larry | (892) 555-8872 | 2312901747      | O268ZZ0       | --4.0.0 -- has a bank account
| 440007 | Sara  | (340) 555-8872 | 3412604728      | 99A843C       | --4.1.1 -- has a bank account
+--------+-------+----------------+-----------------+---------------+
| 626361 | Melissa | (717) 555-1342 | 7834357192      |               | --4.2
+--------+---------+----------------+-----------------+---------------+
| 250277 | James | (676) 555-6554 | 2438825627      | Q13SVG6       | -- 5
+--------+-------+----------------+-----------------+---------------+

-- let's check their bank accounts
SELECT * FROM bank_accounts
JOIN people ON bank_accounts.person_id = people.id
WHERE (people.passport_number = 9029462229
    or people.passport_number = 2312901747
    or people.passport_number = 3412604728
    or people.passport_number = 7834357192
    or people.passport_number = 2438825627
    );


--list of conscripts
+----------------+-----------+---------------+--------+-------+----------------+-----------------+---------------+
| account_number | person_id | creation_year |   id   | name  |  phone_number  | passport_number | license_plate |
+----------------+-----------+---------------+--------+-------+----------------+-----------------+---------------+
| 69638157       | 567218    | 2012          | 567218 | Jack  | (996) 555-8899 | 9029462229      | 52R0Y8U       | --2.0.0
| 72161631       | 251693    | 2015          | 251693 | Larry | (892) 555-8872 | 2312901747      | O268ZZ0       | --4.0.0
| 37409101       | 440007    | 2020          | 440007 | Sara  | (340) 555-8872 | 3412604728      | 99A843C       | --4.1.1
+----------------+-----------+---------------+--------+-------+----------------+-----------------+---------------+


--we have only 2 suspects left and 3 conscripts

-- ITS SUSPECT 4!!
--list of last 2 susopects
SELECT * FROM people WHERE passport_number = 8294398571;
+--------+--------+----------------+-----------------+---------------+
|   id   |  name  |  phone_number  | passport_number | license_plate |
+--------+--------+----------------+-----------------+---------------+
| 560886 | Kelsey | (499) 555-9472 | 8294398571      | 0NTHK55       |
+--------+--------+----------------+-----------------+---------------+

--lets check who withdrew money at this time
SELECT * FROM atm_transactions WHERE account_number = atm_location LIKE '%Leggett%' AND transaction_type = "withdraw" AND day = 28;