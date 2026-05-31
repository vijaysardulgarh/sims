import {
    useEffect,
    useState,
} from 'react';

import api from '../../../../services/api/axios';

const AssetForm = ({
    formData,
    setFormData,
}) => {

    const [
        categories,
        setCategories
    ] = useState([]);

    useEffect(() => {

        loadCategories();

    }, []);

    const loadCategories = async () => {

        try {

            const response =
                await api.get(
                    '/infrastructure/asset-categories/'
                );

            setCategories(
                response.data.results ||
                response.data
            );

        } catch (error) {

            console.error(error);
        }
    };

    return (
        <>
            <div className="mb-3">

                <label>
                    Category
                </label>

                <select
                    className="form-control"
                    value={
                        formData.category || ''
                    }
                    onChange={(e) =>
                        setFormData({
                            ...formData,
                            category:
                                e.target.value,
                        })
                    }
                >
                    <option value="">
                        Select Category
                    </option>

                    {categories.map(
                        (category) => (

                            <option
                                key={category.id}
                                value={category.id}
                            >
                                {category.name}
                            </option>
                        )
                    )}
                </select>

            </div>

            <div className="mb-3">

                <label>
                    Asset Code
                </label>

                <input
                    type="text"
                    className="form-control"
                    value={
                        formData.asset_code || ''
                    }
                    onChange={(e) =>
                        setFormData({
                            ...formData,
                            asset_code:
                                e.target.value,
                        })
                    }
                />

            </div>

            <div className="mb-3">

                <label>
                    Asset Name
                </label>

                <input
                    type="text"
                    className="form-control"
                    value={
                        formData.name || ''
                    }
                    onChange={(e) =>
                        setFormData({
                            ...formData,
                            name:
                                e.target.value,
                        })
                    }
                />

            </div>

            <div className="mb-3">

                <label>
                    Brand
                </label>

                <input
                    type="text"
                    className="form-control"
                    value={
                        formData.brand || ''
                    }
                    onChange={(e) =>
                        setFormData({
                            ...formData,
                            brand:
                                e.target.value,
                        })
                    }
                />

            </div>

            <div className="mb-3">

                <label>
                    Model Number
                </label>

                <input
                    type="text"
                    className="form-control"
                    value={
                        formData.model_number || ''
                    }
                    onChange={(e) =>
                        setFormData({
                            ...formData,
                            model_number:
                                e.target.value,
                        })
                    }
                />

            </div>

            <div className="mb-3">

                <label>
                    Serial Number
                </label>

                <input
                    type="text"
                    className="form-control"
                    value={
                        formData.serial_number || ''
                    }
                    onChange={(e) =>
                        setFormData({
                            ...formData,
                            serial_number:
                                e.target.value,
                        })
                    }
                />

            </div>

            <div className="mb-3">

                <label>
                    Purchase Date
                </label>

                <input
                    type="date"
                    className="form-control"
                    value={
                        formData.purchase_date || ''
                    }
                    onChange={(e) =>
                        setFormData({
                            ...formData,
                            purchase_date:
                                e.target.value,
                        })
                    }
                />

            </div>

            <div className="mb-3">

                <label>
                    Purchase Cost
                </label>

                <input
                    type="number"
                    className="form-control"
                    value={
                        formData.purchase_cost || ''
                    }
                    onChange={(e) =>
                        setFormData({
                            ...formData,
                            purchase_cost:
                                e.target.value,
                        })
                    }
                />

            </div>

            <div className="mb-3">

                <label>
                    Quantity
                </label>

                <input
                    type="number"
                    className="form-control"
                    value={
                        formData.quantity || 1
                    }
                    onChange={(e) =>
                        setFormData({
                            ...formData,
                            quantity:
                                e.target.value,
                        })
                    }
                />

            </div>

            <div className="mb-3">

                <label>
                    Location
                </label>

                <input
                    type="text"
                    className="form-control"
                    value={
                        formData.location || ''
                    }
                    onChange={(e) =>
                        setFormData({
                            ...formData,
                            location:
                                e.target.value,
                        })
                    }
                />

            </div>

            <div className="mb-3">

                <label>
                    Status
                </label>

                <select
                    className="form-control"
                    value={
                        formData.status ||
                        'AVAILABLE'
                    }
                    onChange={(e) =>
                        setFormData({
                            ...formData,
                            status:
                                e.target.value,
                        })
                    }
                >
                    <option value="AVAILABLE">
                        Available
                    </option>

                    <option value="IN_USE">
                        In Use
                    </option>

                    <option value="UNDER_MAINTENANCE">
                        Under Maintenance
                    </option>

                    <option value="DAMAGED">
                        Damaged
                    </option>

                    <option value="DISPOSED">
                        Disposed
                    </option>

                </select>

            </div>

            <div className="mb-3">

                <label>
                    Warranty Expiry
                </label>

                <input
                    type="date"
                    className="form-control"
                    value={
                        formData.warranty_expiry || ''
                    }
                    onChange={(e) =>
                        setFormData({
                            ...formData,
                            warranty_expiry:
                                e.target.value,
                        })
                    }
                />

            </div>

            <div className="mb-3">

                <label>
                    Remarks
                </label>

                <textarea
                    rows="4"
                    className="form-control"
                    value={
                        formData.remarks || ''
                    }
                    onChange={(e) =>
                        setFormData({
                            ...formData,
                            remarks:
                                e.target.value,
                        })
                    }
                />

            </div>
        </>
    );
};

export default AssetForm;