import { Route } from 'react-router-dom';

import RecognitionListPage
    from '../pages/RecognitionListPage';

import RecognitionCreatePage
    from '../pages/RecognitionCreatePage';

import RecognitionEditPage
    from '../pages/RecognitionEditPage';

const recognitionRoutes = (

    <>

        <Route
            path="recognitions"
            element={
                <RecognitionListPage />
            }
        />

        <Route
            path="recognitions/create"
            element={
                <RecognitionCreatePage />
            }
        />

        <Route
            path="recognitions/edit/:id"
            element={
                <RecognitionEditPage />
            }
        />

    </>

);

export default recognitionRoutes;