import pandas as pd

def add_student_to_school(school, i, applicant):
    school.students = pd.concat([
                    school.students,
                    pd.DataFrame([{"rank":i+1, "sex": applicant["sex"], "ability": applicant["ability"]}])
                ], ignore_index=True)
    return school



def multi_school_matching(schools, applicants_df, male_a, female_a):
    male_quota = sum(school.q_male for school in schools)
    female_quota = sum(school.q_female for school in schools)
    n_floating_male = male_a - male_quota
    n_floating_female = female_a - female_quota

    applicants_df = applicants_df.sort_values(by="ability", ascending=False).reset_index(drop=True)

    for i, applicant in applicants_df.iterrows():
        admitted = False
        for school_name in applicant["school_preference"]:
            school = next(s for s in schools if s.name == school_name)
            if applicant["sex"] == "male":
                if school.q_male > 0: # If there is male quota
                    school = add_student_to_school(school, i, applicant)
                    applicants_df.at[i, "admitted_school"] = school.name
                    school.q_male -= 1
                    admitted = True
                    break
                elif school.q_either > 0 and n_floating_male > 0: # If there is either quota is available and there are floating male applicants
                    school = add_student_to_school(school, i, applicant)
                    applicants_df.at[i, "admitted_school"] = school.name
                    school.q_either -= 1
                    n_floating_male -= 1
                    admitted = True
                    break
            elif applicant["sex"] == "female":
                if school.q_female > 0:
                    school = add_student_to_school(school, i, applicant)
                    applicants_df.at[i, "admitted_school"] = school.name
                    school.q_female -= 1
                    admitted = True
                    break
                elif school.q_either > 0 and n_floating_female > 0:
                    school = add_student_to_school(school, i, applicant)
                    applicants_df.at[i, "admitted_school"] = school.name
                    school.q_either -= 1
                    n_floating_female -= 1
                    admitted = True
                    break     
        if not admitted:
            applicants_df.at[i, "admitted_school"] = None
    return schools, applicants_df