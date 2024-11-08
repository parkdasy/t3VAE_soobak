import torch.nn as nn

class Discriminator(nn.Module):
    def __init__(self, m_dim=64, hidden_dims=2000):

        nn.Module.__init__(self)

        self.discriminator = nn.Sequential(
            nn.Linear(m_dim, hidden_dims),
            nn.LeakyReLU(0.2),
            nn.Linear(hidden_dims, hidden_dims),
            nn.LeakyReLU(0.2),
            nn.Linear(hidden_dims, hidden_dims),
            nn.LeakyReLU(0.2),
            nn.Linear(hidden_dims, hidden_dims),
            nn.LeakyReLU(0.2),
            nn.Linear(hidden_dims, hidden_dims),
            nn.LeakyReLU(0.2),
            nn.Linear(hidden_dims, 2),
        )

    def forward(self, z):
        return self.discriminator(z)