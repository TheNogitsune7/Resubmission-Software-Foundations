
import pandas as pd
from Calculation_Functions_New import (
    calculate_mean,
    calculate_median,
    calculate_std_dev,
    calculate_pass_rate,
    calculate_z_scores,
    assign_grade
)

def load_student_scores(file_path):
    return pd.read_csv(file_path)

def process_scores(df, score_column='Score', pass_mark=50):
    scores = df[score_column].dropna().tolist()

    df['Z_score'] = calculate_z_scores(scores)
    df['Grade'] = df[score_column].apply(lambda x: assign_grade(x, pass_mark))
    df['Passed'] = df[score_column] >= pass_mark

    summary = {
        'Mean': calculate_mean(scores),
        'Median': calculate_median(scores),
        'Standard Deviation': calculate_std_dev(scores),
        'Pass Rate (%)': calculate_pass_rate(scores, pass_mark)
    }

    return df, summary

def save_results(df, processed_path, summary, summary_path):
    df.to_csv(processed_path, index=False)
    pd.DataFrame([summary]).to_csv(summary_path, index=False)

def main():
    input_file = "Students.csv"
    processed_file = "Processed_Output.csv"
    summary_file = "Summary_Output.csv"

    try:
        df = load_student_scores(input_file)
        processed_df, stats = process_scores(df)

        print(f"\nProcessed {len(processed_df)} student records.\n")
        for key, value in stats.items():
            print(f"{key}: {value}")

        save_results(processed_df, processed_file, stats, summary_file)
        print(f"\n✔ Processed data saved to: {processed_file}")
        print(f"✔ Summary statistics saved to: {summary_file}")

    except Exception as e:
        print(f"\n❌ Error: {e}")

if __name__ == '__main__':
    main()
