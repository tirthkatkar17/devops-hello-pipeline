"""
monitor.py - Evidently AI Monitoring and Data Quality / Drift Report
Configures Evidently to monitor data metrics for the application.
"""
import os
import sys

# Disable telemetry
os.environ["DO_NOT_TRACK"] = "1"
os.environ["EVIDENTLY_DISABLE_TELEMETRY"] = "1"

import numpy as np
import pandas as pd

def generate_sample_data():
    """Simulate baseline reference and current production data."""
    np.random.seed(42)
    n = 100
    
    ref = pd.DataFrame({
        "input_len": np.random.randint(5, 25, size=n),
        "calc_result": np.random.randint(1, 100, size=n),
        "latency_ms": np.random.normal(loc=30, scale=4, size=n),
        "success": np.random.choice([1, 1, 1, 0], size=n),
    })

    cur = pd.DataFrame({
        "input_len": np.random.randint(5, 28, size=n),
        "calc_result": np.random.randint(1, 105, size=n),
        "latency_ms": np.random.normal(loc=32, scale=5, size=n),
        "success": np.random.choice([1, 1, 1, 1, 0], size=n),
    })
    return ref, cur

def run_evidently_monitor():
    print("=" * 60)
    print("Evidently Tool: Configuring & Running Monitoring Suite")
    print("=" * 60)

    try:
        from evidently.legacy.report import Report
        from evidently.legacy.metric_preset import DataDriftPreset, DataQualityPreset
        from evidently.legacy.test_suite import TestSuite
        from evidently.legacy.tests import TestNumberOfColumns, TestNumberOfRows, TestNumberOfMissingValues
    except ImportError:
        try:
            from evidently.report import Report
            from evidently.metric_preset import DataDriftPreset, DataQualityPreset
            from evidently.test_suite import TestSuite
            from evidently.tests import TestNumberOfColumns, TestNumberOfRows, TestNumberOfMissingValues
        except ImportError:
            from evidently import Report
            from evidently.presets import DataDriftPreset, DataQualityPreset
            from evidently.tests import TestNumberOfColumns, TestNumberOfRows, TestNumberOfMissingValues

    ref_data, cur_data = generate_sample_data()
    print(f"[Evidently] Reference Data Shape: {ref_data.shape}")
    print(f"[Evidently] Current Data Shape:   {cur_data.shape}")

    # Generate Report
    print("\n[1/2] Generating Evidently Monitoring Report...")
    report = Report(metrics=[
        DataDriftPreset(),
        DataQualityPreset(),
    ])
    report.run(reference_data=ref_data, current_data=cur_data)
    report_file = "evidently_report.html"
    report.save_html(report_file)
    print(f" -> Monitoring Report saved to: {os.path.abspath(report_file)}")

    # Generate Test Suite
    print("\n[2/2] Running Evidently Test Suite...")
    suite = TestSuite(tests=[
        TestNumberOfColumns(),
        TestNumberOfRows(),
        TestNumberOfMissingValues(),
    ])
    suite.run(reference_data=ref_data, current_data=cur_data)
    test_file = "evidently_test_suite.html"
    suite.save_html(test_file)
    print(f" -> Test Suite Report saved to: {os.path.abspath(test_file)}")

    print("\n" + "=" * 60)
    print("Evidently Monitor: All Monitoring & Drift checks completed successfully!")
    print("=" * 60)

if __name__ == "__main__":
    run_evidently_monitor()
