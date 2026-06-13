import api
    from '../../../../services/api/axios';

export const ENDPOINT =
    '/infrastructure/rooms/';

const roomPaletteService = {

    getAll: () =>

        api.get(
            ENDPOINT
        ),

};

export default roomPaletteService;