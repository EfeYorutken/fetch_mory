fetch mori is a CLI tool to visualised how much time you have spent alive and maybe more importantly
how much time you have left.
It should be noted that the "days to live" is calculated bades on the average life expectency of a person.

# How to use
1. Open up the `config.json` file
1. enter your date of birth in the `birth_date` filed
1. it you choose, enter additional measurements of time into the `measurements` object
    - each measurement should be mapped to how many human __days__ each unit of measurement reprensent. for example, a week has 7 days in it, hence is mapped to 7
    - for displaying purposses, it is recomended to name filelds as plural: weeks insetad of week, years instead of year etc
1. adjust the fields in the `display` field to tailor the output
char\_per\_line : how many characters will be printed to the screen before going to the next line
char\_lived : the char that represents the days you have lived
char\_to\_live : the char that represents the days you have to live
motion\_over\_time : what is going to be the time difference between each character displayed
