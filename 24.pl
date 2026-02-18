% -------- FACTS --------

% Diseases
disease(diabetes).
disease(hypertension).
disease(obesity).
disease(anemia).
disease(heart_problem).

% Diet suggestions
diet(diabetes, low_sugar_diet).
diet(diabetes, high_fiber_food).
diet(diabetes, avoid_sweets).

diet(hypertension, low_salt_diet).
diet(hypertension, fruits_and_vegetables).
diet(hypertension, avoid_processed_food).

diet(obesity, low_calorie_diet).
diet(obesity, high_protein_diet).
diet(obesity, regular_exercise).

diet(anemia, iron_rich_food).
diet(anemia, green_leafy_vegetables).
diet(anemia, vitamin_c_food).

diet(heart_problem, low_fat_diet).
diet(heart_problem, avoid_oily_food).
diet(heart_problem, omega_3_food).

% -------- RULE --------

suggest_diet(Disease, Diet) :-
    disease(Disease),
    diet(Disease, Diet).
