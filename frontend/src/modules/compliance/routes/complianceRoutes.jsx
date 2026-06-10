import { Route } from "react-router-dom";

import affiliationRoutes
    from "../affiliations/routes/affiliationRoutes";

import certificateRoutes
    from "../certificates/routes/certificateRoutes";

import complianceDocumentRoutes
    from "../compliance-documents/routes/complianceDocumentRoutes";

import inspectionRoutes
    from "../inspections/routes/inspectionRoutes";

import mandatoryPublicDisclosureRoutes
    from "../mandatory-public-disclosures/routes/mandatoryPublicDisclosureRoutes";

import recognitionRoutes
    from "../recognitions/routes/recognitionRoutes";

const complianceRoutes = (

    <Route path="compliance">

        {mandatoryPublicDisclosureRoutes}

        {complianceDocumentRoutes}

        {affiliationRoutes}

        {recognitionRoutes}

        {certificateRoutes}

        {inspectionRoutes}

    </Route>

);

export default complianceRoutes;