import api
    from '../../../../services/api/axios';

export const ENDPOINT =
    '/academics/subjects/';

const subjectPaletteService = {

    getAll: () =>

        api.get(
            ENDPOINT
        ),

};

export default subjectPaletteService;