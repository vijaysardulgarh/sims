import api from '../../../../services/api/axios';

const endpoint =
    '/communications/communication-templates/';

export const getCommunicationTemplates = () =>
    api.get(endpoint);

export const getCommunicationTemplate = (id) =>
    api.get(`${endpoint}${id}/`);

export const createCommunicationTemplate = (
    data
) =>
    api.post(endpoint, data);

export const updateCommunicationTemplate = (
    id,
    data
) =>
    api.put(
        `${endpoint}${id}/`,
        data
    );

export const deleteCommunicationTemplate = (
    id
) =>
    api.delete(
        `${endpoint}${id}/`
    );