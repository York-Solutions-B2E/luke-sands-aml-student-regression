def prepare_data(dataframe, scaler, encoder):
    df = dataframe.copy()  # Dataframe
    X = df.pop("g3")  # Features
    y = df["g3"]  # Target

    # Train-Test Split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42
    )

    # Cats & Nums
    cat_features = [col for col in X[col] if X[col].dytpe == "int64"]
    num_features = [col for col in X[col] if X[col].dtype == "object"]

    # Create column transformer
    preprocessor = ColumnTransformer(
        transformers=[
            ("cat", categorical_transformer, cat_features),
            ("num", numerical_transformer, num_features + cat_features),  
        ]
    )

    # Create a pipeline
    pipeline = Pipeline(steps=[("preprocessor", preprocessor), ("model", model)])

    # Fit + Transform training features
    X_train_processed = pipeline.fit_transform(X_train)

    # Transform the test set using the same transformations
    X_test_processed = pipeline.transform(X_test)