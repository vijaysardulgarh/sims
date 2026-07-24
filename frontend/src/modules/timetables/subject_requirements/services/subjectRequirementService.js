import axios from 'axios';

const API_BASE_URL = 'http://127.0.0.1:8000'; 

const apiClient = axios.create({
    baseURL: API_BASE_URL,
});

apiClient.interceptors.request.use(
    (config) => {
        const token = localStorage.getItem('access') || localStorage.getItem('token');
        if (token) {
            config.headers.Authorization = `Bearer ${token}`;
        }
        return config;
    },
    (error) => Promise.reject(error)
);

export const SubjectRequirementService = {
    // Classes, Streams, and Subjects remain under academics
    getClasses: () => apiClient.get('/api/academics/classes/'),
    getStreams: () => apiClient.get('/api/academics/streams/'),
    getSubjects: () => apiClient.get('/api/academics/subjects/'),

    // Subject requirements are routed under timetables based on your urls.py
    getRequirements: (classId, streamId) => {
        let url = `/api/timetables/subject-requirements/bulk_assign/?school_class=${classId}`;
        if (streamId) url += `&stream=${streamId}`;
        return apiClient.get(url);
    },

    saveRequirements: (payload) => {
        return apiClient.post('/api/timetables/subject-requirements/bulk_assign/', payload);
    }
};