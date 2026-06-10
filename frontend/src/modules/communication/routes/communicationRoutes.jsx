import { Route } from 'react-router-dom';

import communicationCategoryRoutes
    from '../communication-categories/routes/communicationCategoryRoutes';

import communicationTemplateRoutes
    from '../communication-templates/routes/communicationTemplateRoutes';

import notificationRoutes
    from '../notifications/routes/notificationRoutes';

import circularRoutes
    from '../circulars/routes/circularRoutes';

import noticeRoutes
    from '../notices/routes/noticeRoutes';

import newsRoutes
    from '../news/routes/newsRoutes';

import eventRoutes
    from '../events/routes/eventRoutes';

import faqRoutes
    from "../faqs/routes/faqRoutes";    

const communicationRoutes = (

    <Route path="communications">

        {communicationCategoryRoutes}

        {communicationTemplateRoutes}

        {notificationRoutes}

        {circularRoutes}

        {noticeRoutes}

        {newsRoutes}

        {eventRoutes}
        
        {faqRoutes}
    </Route>

);

export default communicationRoutes;