import pandas as pd
df_snacks = pd.read_csv('snacks.csv')
df_exercise = pd.read_csv('exercise.csv')

df_snacks['key'] = df_snacks['key'].str.strip()
df_exercise['key'] = df_exercise['key'].str.strip()


snacks  =  df_snacks.set_index('key')[['kcal','serving']].to_dict('index')
exercise = dict(zip(df_exercise['key'], df_exercise['kcal_p_m']))
max_minute = 30

total = 0
first_entry = True
while True:
    prompt = 'Hello, please enter what you want to snack on today\n>>' if first_entry else 'anything else?\n(enter "c" to continue)\n>>'
    snack_input = input(prompt)
    first_entry = False
    if snack_input in snacks:
        kcal = snacks[snack_input]['kcal']
        serving = snacks[snack_input]['serving']
        total = total + kcal
        print(f'{snack_input} : {kcal}kcal / {serving}')
    elif snack_input == 'c':
        prompt = f'You will consume {total} kcal for today\nSee below for exercises you can do to be less guilty\n'
        print(prompt)
        break
for exercise_type,kcal_goal in exercise.items():
    if total // kcal_goal < max_minute:
        print(f'{exercise_type}:\n{int(total//kcal_goal):} minutes = {int(kcal_goal)*int(total//kcal_goal)} kcal total burn\n')




