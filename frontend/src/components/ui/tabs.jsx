const Tabs = ({
    tabs = [],
    activeTab,
    onChange,
}) => {
    return (
        <div
            className="
                border-b
                flex
                gap-1
                overflow-x-auto
            "
        >
            {tabs.map((tab) => (
                <button
                    key={tab}
                    onClick={() =>
                        onChange(tab)
                    }
                    className={`
                        px-4
                        py-3
                        whitespace-nowrap
                        border-b-2
                        transition
                        ${
                            activeTab === tab
                                ? "border-blue-600 text-blue-600 font-medium"
                                : "border-transparent text-gray-500 hover:text-gray-700"
                        }
                    `}
                >
                    {tab}
                </button>
            ))}
        </div>
    );
};

export default Tabs;