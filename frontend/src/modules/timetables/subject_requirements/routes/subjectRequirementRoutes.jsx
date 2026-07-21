import { Route } from "react-router-dom";
import SubjectRequirementMatrixPage from "../pages/SubjectRequirementMatrixPage";

const subjectRequirementRoutes = (
  <Route path="subject-requirements">
    <Route index element={<SubjectRequirementMatrixPage />} />
  </Route>
);

export default subjectRequirementRoutes;