import pandas

maindata = pandas.read_csv('../files/deadside_data.csv',
                           header=None,
                           names=['timestamp',
                                  'hunter',
                                  'hunter_UID',
                                  'victim',
                                  'victim_UID',
                                  'weapon',
                                  'range',
                                  'blank'
                                  ],
                           delimiter=';'
                           )


def marksman_award():
    """Find the username with the longest range kill"""
    return maindata.loc[maindata['range'].idxmax()]


def bloodthirsty_award():
    """Find the top kills"""
    agg_data = maindata.groupby(['hunter']).size().reset_index(name='counts').sort_values('counts').tail(1)
    return agg_data


def bullet_sponge_award():
    """Most deaths"""
    agg_data = maindata.groupby(['victim']).size().reset_index(name='counts').sort_values('counts').tail(1)
    return agg_data


def kill_death_ratio():
    kills = maindata.groupby(['hunter']).size().reset_index(name='kills')
    deaths = maindata.groupby(['victim']).size().reset_index(name='deaths').rename(columns={'victim': 'hunter'})
    kdr_df = kills.join(deaths.set_index('hunter'), on='hunter')
    for idx, row in kdr_df.iterrows():
        kdr_df.at[idx, 'ratio'] = round(row['kills'] / row['deaths'], 2)
    return kdr_df


def bully():
    """Show the most common hunter-victim pairing"""
    bully_df = maindata.groupby(['hunter', 'victim']).size().reset_index(name='counts')
    return bully_df.loc[bully_df['counts'].idxmax()]


def punching_bag():
    """Show the victim with the most distinct hunters"""
    victim_df = maindata.groupby(['victim', 'hunter']).count()
    victim_df1 = victim_df.groupby(['hunter']).sum()
    # print(victim_df)
    # for idx, row in victim_df.iteritems():
    #     pass
    return True


if __name__ == '__main__':
    print(bloodthirsty_award())
    print(bullet_sponge_award())
    print(kill_death_ratio())
    print(str(marksman_award()))
    print(bully())
    print(punching_bag())
