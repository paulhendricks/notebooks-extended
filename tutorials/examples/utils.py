def load_names_dataset(filepath_glob):
    dtypes = OrderedDict([
        ("seller_name", "category"),
        ("new", "category"),
    ])
    
    
    df = dask_cudf.read_csv(filepath_glob, delimiter='|', 
                            names=list(dtypes.keys()), dtype=list(dtypes.values()))
    
    return df


def load_acquisition_dataset(filepath_glob):
    acquisition_dtypes = OrderedDict([
        ('loan_id', 'int64'),
        ('orig_channel', 'category'),
        ('seller_name', 'category'),
        ('orig_interest_rate', 'float64'),
        ('orig_upb', 'int64'),
        ('orig_loan_term', 'int64'),
        ('orig_date', 'date'),
        ('first_pay_date', 'date'),
        ('orig_ltv', 'float64'),
        ('orig_cltv', 'float64'),
        ('num_borrowers', 'float64'),
        ('dti', 'float64'),
        ('borrower_credit_score', 'float64'),
        ('first_home_buyer', 'category'),
        ('loan_purpose', 'category'),
        ('property_type', 'category'),
        ('num_units', 'int64'),
        ('occupancy_status', 'category'),
        ('property_state', 'category'),
        ('zip', 'int64'),
        ('mortgage_insurance_percent', 'float64'),
        ('product_type', 'category'),
        ('coborrow_credit_score', 'float64'),
        ('mortgage_insurance_type', 'float64'),
        ('relocation_mortgage_indicator', 'category')
    ])
    
    
    df = dask_cudf.read_csv(filepath_glob, delimiter='|', 
                            names=list(dtypes.keys()), dtype=list(dtypes.values()))
    
    return df


def load_performance_dataset(filepath_glob):
    dtypes = OrderedDict([
            ('loan_id', 'int64'),
            ('monthly_reporting_period', 'date'),
            ('servicer', 'category'),
            ('interest_rate', 'float64'),
            ('current_actual_upb', 'float64'),
            ('loan_age', 'float64'),
            ('remaining_months_to_legal_maturity', 'float64'),
            ('adj_remaining_months_to_maturity', 'float64'),
            ('maturity_date', 'date'),
            ('msa', 'float64'),
            ('current_loan_delinquency_status', 'int32'),
            ('mod_flag', 'category'),
            ('zero_balance_code', 'category'),
            ('zero_balance_effective_date', 'date'),
            ('last_paid_installment_date', 'date'),
            ('foreclosed_after', 'date'),
            ('disposition_date', 'date'),
            ('foreclosure_costs', 'float64'),
            ('prop_preservation_and_repair_costs', 'float64'),
            ('asset_recovery_costs', 'float64'),
            ('misc_holding_expenses', 'float64'),
            ('holding_taxes', 'float64'),
            ('net_sale_proceeds', 'float64'),
            ('credit_enhancement_proceeds', 'float64'),
            ('repurchase_make_whole_proceeds', 'float64'),
            ('other_foreclosure_proceeds', 'float64'),
            ('non_interest_bearing_upb', 'float64'),
            ('principal_forgiveness_upb', 'float64'),
            ('repurchase_make_whole_proceeds_flag', 'category'),
            ('foreclosure_principal_write_off_amount', 'float64'),
            ('servicing_activity_indicator', 'category')
        ])
    
    
    df = dask_cudf.read_csv(filepath_glob, delimiter='|', 
                            names=list(dtypes.keys()), dtype=list(dtypes.values()))
    
    return df
