% -------- SYMPTOMS --------

symptom(fever).
symptom(cough).
symptom(headache).
symptom(sore_throat).
symptom(body_pain).
symptom(sneezing).
symptom(chest_pain).
symptom(fatigue).

% -------- DISEASE RULES --------

disease(flu) :-
    symptom(fever),
    symptom(cough),
    symptom(body_pain).

disease(cold) :-
    symptom(sneezing),
    symptom(sore_throat),
    symptom(cough).

disease(migraine) :-
    symptom(headache),
    symptom(fatigue).

disease(covid) :-
    symptom(fever),
    symptom(cough),
    symptom(fatigue),
    symptom(chest_pain).

% -------- DIAGNOSIS --------

diagnose(Disease) :-
    disease(Disease),
    write('You may have: '),
    write(Disease).
