const PageHeader = ({
    title,
    subtitle,
    actions,
    breadcrumbs = [],
}) => {

    return (

        <div
            className="
                flex
                flex-col
                md:flex-row
                md:items-center
                md:justify-between
                gap-4
                mb-6
            "
        >

            <div>

                {/* Breadcrumbs */}

                {breadcrumbs.length > 0 && (

                    <div
                        className="
                            text-sm
                            text-gray-500
                            mb-2
                        "
                    >

                        {breadcrumbs.map(
                            (
                                item,
                                index
                            ) => (
                                <span
                                    key={item}
                                >
                                    {item}

                                    {index <
                                        breadcrumbs.length -
                                            1 &&
                                        " > "}
                                </span>
                            )
                        )}

                    </div>

                )}

                {/* Title */}

                <h1
                    className="
                        text-2xl
                        font-bold
                    "
                >
                    {title}
                </h1>

                {/* Subtitle */}

                {subtitle && (
                    <p
                        className="
                            text-gray-500
                            mt-1
                        "
                    >
                        {subtitle}
                    </p>
                )}

            </div>

            {/* Actions */}

            <div>
                {actions}
            </div>

        </div>

    );
};

export default PageHeader;